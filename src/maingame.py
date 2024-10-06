import os
import random
import math
import pygame
import sys

from everythingbutmain.features import insert_img, insert_imgs, Liveliness
from everythingbutmain.systems import PhysMath, Character, Rival
from everythingbutmain.map import Map
from everythingbutmain.sadows import Shadows
from everythingbutmain.fragments import Fragment
from everythingbutmain.speck import Speck


class Main:
    def __init__(self):
        pygame.init()
        # the title of the window for the game
        pygame.display.set_caption('A dogs Journey')
        # the window size for the game
        self.window = pygame.display.set_mode((640, 480))
        # the one that we render onto
        self.show = pygame.Surface((320, 240), pygame.SRCALPHA)
        # without background and outlines
        self.show_two = pygame.Surface((320, 240))

        self.time = pygame.time.Clock()
        self.motion = [False, False]

        self.aids = {
            'decor': insert_imgs('tiles/decor'),
            'grass': insert_imgs('tiles/grass'),
            'large_decor': insert_imgs('tiles/large_decor'),
            'stone': insert_imgs('tiles/stone'),
            'player': insert_img('entities/player.png'),
            'background': insert_img('background.png'),
            'clouds': insert_imgs('clouds'),
            'enemy/idle': Liveliness(insert_imgs('entities/enemy/idle'), pic_duration=6),
            'enemy/run': Liveliness(insert_imgs('entities/enemy/run'), pic_duration=4),
            'player/idle': Liveliness(insert_imgs('entities/player/idle'), pic_duration=6),
            'player/run': Liveliness(insert_imgs('entities/player/run'), pic_duration=4),
            'player/jump': Liveliness(insert_imgs('entities/player/jump')),
            'player/slide': Liveliness(insert_imgs('entities/player/slide')),
            'player/wall_slide': Liveliness(insert_imgs('entities/player/wall_slide')),
            'particles/leaf': Liveliness(insert_imgs('particles/leaf'), pic_duration=20, circle=False),
            'particles/particle': Liveliness(insert_imgs('particles/particle'), pic_duration=6, circle=False),
            'gun': insert_img('gun.png'),
            'projectile': insert_img('projectile.png'),
        }

        self.sounds = {
            'jump': pygame.mixer.Sound('data/sfx/jump.wav'),
            'dash': pygame.mixer.Sound('data/sfx/dash.wav'),
            'hit': pygame.mixer.Sound('data/sfx/hit.wav'),
            'shoot': pygame.mixer.Sound('data/sfx/shoot.wav'),
            'ambience': pygame.mixer.Sound('data/sfx/ambience.wav'),
        }

        self.sounds['ambience'].set_volume(0.2)
        self.sounds['shoot'].set_volume(0.4)
        self.sounds['hit'].set_volume(0.8)
        self.sounds['dash'].set_volume(0.3)
        self.sounds['jump'].set_volume(0.7)

        self.shadows = Shadows(self.aids['clouds'], tally=16)

        self.character = Character(self, (50, 50), (8, 15))

        self.maps = Map(self, brick_bigness=16)

        self.step = 0
        self.putin_step(self.step)

        self.window_sway = 0

    def putin_step(self, chart):
        """this loads in different maps"""
        self.maps.putin('data/maps/' + str(chart) + '.json')

        self.needle_enters = []
        """allows for particles to fall from a tree"""
        for bush in self.maps.removal([('large_decor', 2)], remain=True):
            self.needle_enters.append(pygame.Rect(4 + bush['pos'][0], 4 + bush['pos'][1], 23, 13))

        self.rivals = []
        """just get the location to put stuff there (not keep the info)"""
        for invade in self.maps.removal([('spawners', 0), ('spawners', 1)]):
            if invade['variant'] == 0:
                self.character.pos = invade['pos']
                self.character.air_time = 0
            else:
                self.rivals.append(Rival(self, invade['pos'], (8, 15)))

        self.missiles = []
        self.fragments = []
        self.speck = []

        # camera
        self.scrawl = [0, 0]
        self.deceased = 0

        self.conversion = -30

    def sprint(self):
        """controls the game and adds in music"""
        pygame.mixer.music.load('data/music.wav')
        # wav will work with pygame better then others
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.sounds['ambience'].play(-1)

        """controls the game and runs it"""""
        while True:
            self.show.fill((0, 0, 0, 0))

            self.show_two.blit(self.aids['background'], (0, 0))

            self.window_sway = max(0, self.window_sway - 1)

            if not len(self.rivals):
                self.conversion += 1
                if self.conversion > 30:
                    self.step = min(self.step + 1, len(os.listdir('data/maps')) - 1)
                    self.putin_step(self.step)
            if self.conversion < 0:
                self.conversion += 1

            if self.deceased:
                self.deceased += 1
                if self.deceased == 10:
                    self.conversion = min(30, self.conversion + 1)
                # restarts after you die (after 40 frames it will restart)
                if self.deceased > 40:
                    self.putin_step(self.step)

            # x axis
            self.scrawl[0] += (self.character.rectangle().centerx - self.show.get_width() / 2 - self.scrawl[0]) / 30
            # y axis
            self.scrawl[1] += (self.character.rectangle().centery - self.show.get_height() / 2 - self.scrawl[1]) / 30

            transition_scrawl = (int(self.scrawl[0]), int(self.scrawl[1]))

            """have the span rate for leaves be proportional to the amount of pixels that hit box covers
            (bigger tree = more leaves)"""
            for rectangle in self.needle_enters:
                if random.random() * 49999 < rectangle.width * rectangle.height:
                    position = (rectangle.x + random.random() * rectangle.width, rectangle.y + random.random() * rectangle.height)
                    self.fragments.append(Fragment(self, 'leaf', position, quickness=[-0.1, 0.3], structure=random.randint(0, 20)))

            self.shadows.version()
            self.shadows.translate(self.show_two, counteract=transition_scrawl)

            self.maps.translate(self.show, counteract=transition_scrawl)

            """allows you to kill the enemy and the enemy is removed from the board"""
            for rival in self.rivals.copy():
                dead = rival.version(self.maps, (0, 0))
                rival.translate(self.show, counteract=transition_scrawl)
                if dead:
                    self.rivals.remove(rival)

            if not self.deceased:
                self.character.version(self.maps, (self.motion[1] - self.motion[0], 0))
                self.character.translate(self.show, counteract=transition_scrawl)

            """allows shooting and accounts for solid walls and killing the character"""
            for missile in self.missiles.copy():
                missile[0][0] += missile[1]
                missile[2] += 1
                pic = self.aids['projectile']
                self.show.blit(pic, (missile[0][0] - pic.get_width() / 2 - transition_scrawl[0], missile[0][1] - pic.get_height() / 2 - transition_scrawl[1]))
                if self.maps.firm_examine(missile[0]):
                    self.missiles.remove(missile)
                    """adding in spark for when it hits a wall"""
                    for i in range(4):
                        self.speck.append(Speck(missile[0], random.random() - 0.5 + (math.pi if missile[1] > 0 else 0), 2 + random.random()))
                elif missile[2] > 360:
                    self.missiles.remove(missile)

                elif abs(self.character.rushing) < 50:
                    if self.character.rectangle().collidepoint(missile[0]):
                        self.missiles.remove(missile)

                        self.deceased += 1
                        self.sounds['hit'].play()
                        self.window_sway = max(16, self.window_sway)
                        """when it hits the player and players death"""
                        for i in range(30):
                            slant = random.random() * math.pi * 2
                            pace = random.random() * 5
                            self.speck.append(Speck(self.character.rectangle().center, slant, 2 + random.random()))
                            self.fragments.append(Fragment(self, 'particle', self.character.rectangle().center, quickness=[math.cos(slant + math.pi) * pace * 0.5, math.sin(slant + math.pi) * pace * 0.5], structure=random.randint(0, 7)))

            """managing sparks and how they should react to different things"""
            for speck in self.speck.copy():
                dead = speck.version()
                speck.translate(self.show, counteract=transition_scrawl)
                if dead:
                    self.speck.remove(speck)
            show_veil = pygame.mask.from_surface(self.show)
            show_outline = show_veil.to_surface(setcolor=(0, 0, 0, 180), unsetcolor=(0, 0, 0, 0))
            """have the outline be a little bigger"""
            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                self.show_two.blit(show_outline, offset)

            """manage particles"""
            for fragment in self.fragments.copy():
                dead = fragment.version()
                fragment.translate(self.show, counteract=transition_scrawl)
                if fragment.type == 'leaf':
                    fragment.pos[0] += math.sin(fragment.animation.frame * 0.035) * 0.3
                if dead:
                    self.fragments.remove(fragment)

            """all of the buttons you can press and what the game should do"""
            for incident in pygame.event.get():
                if incident.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if incident.type == pygame.KEYDOWN:
                    if incident.key == pygame.K_LEFT:
                        self.motion[0] = True
                    if incident.key == pygame.K_RIGHT:
                        self.motion[1] = True
                    if incident.key == pygame.K_UP:
                        if self.character.leap():
                            self.sounds['jump'].play()
                    if incident.key == pygame.K_x:
                        self.character.rush()
                if incident.type == pygame.KEYUP:
                    if incident.key == pygame.K_LEFT:
                        self.motion[0] = False
                    if incident.key == pygame.K_RIGHT:
                        self.motion[1] = False

            if self.conversion:
                # the transition
                change_surface = pygame.Surface(self.show.get_size())
                pygame.draw.circle(change_surface, (255, 255, 255), (self.show.get_width() // 2, self.show.get_height() // 2), (30 - abs(self.conversion)) * 8)
                change_surface.set_colorkey((255, 255, 255))
                self.show.blit(change_surface, (0, 0))
            self.show_two.blit(self.show, (0, 0))

            window_counteract = (random.random() * self.window_sway - self.window_sway / 2, random.random() * self.window_sway - self.window_sway / 2)
            self.window.blit(pygame.transform.scale(self.show_two, self.window.get_size()), window_counteract)
            pygame.display.update()
            self.time.tick(60)  # 60 fps


Main().sprint()


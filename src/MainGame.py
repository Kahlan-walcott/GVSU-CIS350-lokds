from Sprites import Avatar, AnimationSequence
from FunkyFeatures import Artifacts, NPCs, NPCMessage
from AdvancedMovement import Ghosts, ObstacleFloat
import sys
import json
import pygame
import os

BASE_IMAGE_DIR = 'artifacts/images/'


def load_picture(file):
    picture = pygame.image.load(BASE_IMAGE_DIR + file).convert()
    picture.set_colorkey((0, 0, 0))
    return picture


def load_pictures(file):
    pictures = []
    png_filesNjpg_Files = [f for f in os.listdir(BASE_IMAGE_DIR + file) if f.endswith('.png') or f.endswith('.jpg')]
    for img_name in sorted(png_filesNjpg_Files):
        pictures.append(load_picture(file + '/' + img_name))
    if os.path.exists(BASE_IMAGE_DIR + file):
        print(f"File exists: {BASE_IMAGE_DIR + file}")
    return pictures


ADJACENT_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}


class Adventure:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Dog\'s Journey Home')

        self.channel1 = pygame.mixer.Channel(0)
        self.channel1.set_volume(0.1)  # Set volume to 20% of maximum
        self.channel1.play(pygame.mixer.Sound('artifacts/backgroundmusic.mp3'))

        self.channel2 = pygame.mixer.Channel(1)
        self.channel2.set_volume(0.2)

        self.channel3 = pygame.mixer.Channel(2)
        self.channel3.set_volume(0.2)

        #self.channel2.play(pygame.mixer.Sound('artifacts/artifacts_falling.mp3'))



        #pygame.mixer.music.play(-1)

        self.tile_dimension = 16
        self.tile_layout = {}
        self.exterior_tiles = []
        self.window = pygame.display.set_mode((640, 480))
        self.render_surface = pygame.Surface((320, 240))
        self.character_type = 'avatar'
        self.timer = pygame.time.Clock()
        self.movement_status = [False, False]
        self.resources = {
            'decor': load_pictures('tiles/decor'),
            'grass': load_pictures('tiles/grass'),
            'large_decor': load_pictures('tiles/large_decor'),
            'stone': load_pictures('tiles/stone'),
            'player': load_picture('entities/player/player.png'),
            'background': load_picture('background.jpg'),
            'water': load_pictures('tiles/water'),
            'artifacts': load_pictures('artifacts'),
            'player/thing': AnimationSequence(load_pictures('entities/player/thing')),
            'player/run': AnimationSequence(load_pictures('entities/player/run'), 4),
            'NPC/tomato': load_pictures('entities/NPC/tomato'),
            'float': load_pictures('float'),
            'ghost/down' : AnimationSequence(load_pictures('entities/ghost/down'), 0.5),
            'ghost/up': AnimationSequence(load_pictures('entities/ghost/up'), 0.5),
            'ghost/left': AnimationSequence(load_pictures('entities/ghost/left'), 0.5),
            'ghost/right': AnimationSequence(load_pictures('entities/ghost/right'),0.5)


        }
        self.load_game('map.json')
        self.scroll_offset = [0, 0]
        self.avatar = Avatar(self, 'player', (0, 0), (10, 10), 'thing')
        self.artifacts = Artifacts(self)
        self.tomato = NPCs(self, 'NPC/tomato')
        self.current_animation = self.resources['player/thing'].duplicate()
        self.current_action = 'thing'
        self.message = NPCMessage(self, 419, 20, False)
        self.ghosts = Ghosts(self)
        self.obstacle = ObstacleFloat(self, 'float')

    def surrounding_tiles(self, position):
        tiles = []
        tile_position = (int(position[0] // self.tile_dimension), int(position[1] // self.tile_dimension))
        for offset in ADJACENT_OFFSETS:
            check_position = str(tile_position[0] + offset[0]) + ';' + str(tile_position[1] + offset[1])
            if check_position in self.tile_layout:
                tiles.append(self.tile_layout[check_position])
        return tiles

    def save_game(self, file):
        f = open(file, 'w')
        json.dump({'tile_layout': self.tile_layout, 'tile_dimension': self.tile_dimension,
                   'exterior_tiles': self.exterior_tiles}, f)
        f.close()

    def load_game(self, file):
        f = open(file, 'r')
        level_data = json.load(f)
        f.close()
        self.tile_layout = level_data['tilemap']
        self.tile_dimension = level_data['tile_size']
        self.exterior_tiles = level_data['offgrid']

    def physics_rectangles(self, position):
        rectangles = []
        for tile in self.surrounding_tiles(position):
            if tile['type'] in PHYSICS_TILES:
                rectangles.append(
                    pygame.Rect(tile['pos'][0] * self.tile_dimension, tile['pos'][1] * self.tile_dimension,
                                self.tile_dimension, self.tile_dimension)
                )
        return rectangles

    def render(self, surface, offset=(0, 0)):
        for tile in self.exterior_tiles:
            surface.blit(self.resources[tile['type']][tile['variant']],
                         (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))
        for x in range(offset[0] // self.tile_dimension, (offset[0] + surface.get_width()) // self.tile_dimension + 1):
            for y in range(offset[1] // self.tile_dimension,
                           (offset[1] + surface.get_height()) // self.tile_dimension + 1):
                location = str(x) + ';' + str(y)
                if location in self.tile_layout:
                    tile = self.tile_layout[location]
                    surface.blit(self.resources[tile['type']][tile['variant']],
                                 (tile['pos'][0] * self.tile_dimension - offset[0],
                                  tile['pos'][1] * self.tile_dimension - offset[1]))

    def run(self):
        while True:

            self.render_surface.blit(self.resources['background'], (0, 0))
            # self.render_surface.blit(self.resources['artifacts'][0], (300,110))
            #print(self.avatar.position[0], self.avatar.position[1])
            if self.avatar.avatar_velocity[1] > 1:
                
                    # Check if the sound is not already playing
                if not self.channel3.get_busy():
                    self.channel3.play(pygame.mixer.Sound('artifacts/artifacts_falling.mp3'))

            print(self.avatar.avatar_velocity)
            if self.avatar.position[1] >= 500:
                Adventure().run()
            self.scroll_offset[0] += (self.avatar.rect().centerx - self.render_surface.get_width() / 2 -
                                      self.scroll_offset[0]) / 30
            self.scroll_offset[1] += (self.avatar.rect().centery - self.render_surface.get_height() / 2 -
                                      self.scroll_offset[1]) / 30
            render_scroll = (int(self.scroll_offset[0]), int(self.scroll_offset[1]))
            self.obstacle.drawObstacle(self.render_surface, distanceFromCamera=render_scroll)
            self.tomato.drawNPC(self.render_surface, distanceFromCamera=render_scroll)
            self.render(self.render_surface, offset=render_scroll)
            self.avatar.update_avatar(self.tile_layout, (self.movement_status[1] - self.movement_status[0], 0))
            self.avatar.render(self.render_surface, offset=render_scroll)

            self.artifacts.drawArtifacts(self.render_surface, distanceFromCamera=render_scroll)
            if self.tomato.check_collision_with_NPC(self.avatar.rect(), self.render_surface,
                                                    distanceFromCamera=render_scroll):
                self.message.drawMessage(self.render_surface, distanceFromCamera=render_scroll)
            pygame.display.update()
            self.artifacts.check_collision_with_artifacts(self.avatar.rect())
            self.ghosts.draw_ghosts(self.render_surface, distanceFromCamera=render_scroll)
            self.ghosts.check_collision_with_ghosts(self.avatar.rect())
            if self.ghosts.check_collision_with_ghosts(self.avatar.rect()):
                Adventure().run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement_status[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement_status[1] = True
                    if event.key == pygame.K_UP:
                        self.channel2.play(pygame.mixer.Sound('artifacts/jump-sound.mp3'))
                        self.avatar.avatar_velocity[1] = -2
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement_status[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement_status[1] = False
            self.window.blit(pygame.transform.scale(self.render_surface, self.window.get_size()), (0, 0))
            pygame.display.update()

            self.timer.tick(60)


Adventure().run()



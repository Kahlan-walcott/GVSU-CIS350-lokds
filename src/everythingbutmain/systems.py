import math
import random

import pygame
from everythingbutmain.fragments import Fragment
from everythingbutmain.speck import Speck


class PhysMath:

    """
    controls the pysics of falling and solid tiles
    """

    def __init__(self, maingame, variety, position, bigness):
        self.main = maingame
        self.variety = variety
        self.position = list(position)
        self.bigness = bigness
        # updating based of the acceleration
        self.quickness = [0, 0]
        self.crash = {'up': False, 'down': False, 'right': False, 'left': False}

        self.activity = ''
        self.movement_counter = (-3, -3)
        self.invert = False
        self.calibrate_activity('idle')

        self.final_gestore = [0, 0]

    def rectangle(self):
        """gets a fresh rect based on our position"""
        return pygame.Rect(self.position[0], self.position[1], self.bigness[0], self.bigness[1])

    def calibrate_activity(self, activity):
        """sets or resets the characters action"""
        if activity != self.activity:
            self.activity = activity
            self.gestore = self.main.assets[self.variety + '/' + self.activity].copy()

    def version(self, maps, gestore=(0, 0)):
        """makes the character flip left or right based on which direction the character is going"""

        self.crash = {'up': False, 'down': False, 'right': False, 'left': False}

        scene_gester = (gestore[0] + self.quickness[0], gestore[1] + self.quickness[1])

        self.position[0] += scene_gester[0]

        structure_rectangle = self.rectangle()
        """controls collisions in the x axis focusing on the rectangles position"""
        for rectangle in maps.physrectangle_surrounding(self.position):
            if structure_rectangle.colliderect(rectangle):
                if scene_gester[0] > 0:
                    structure_rectangle.right = rectangle.left
                    self.crash['right'] = True
                if scene_gester[0] < 0:
                    structure_rectangle.left = rectangle.right
                    self.crash['left'] = True

                self.position[0] = structure_rectangle.x

        self.position[1] += scene_gester[1]

        structure_rectangle = self.rectangle()
        """for collisions in the y axis"""
        for rectangles in maps.physrectangle_surrounding(self.position):
            if structure_rectangle.colliderect(rectangles):
                if scene_gester[1] > 0:
                    structure_rectangle.bottom = rectangles.top
                    self.crash['down'] = True
                if scene_gester[1] < 0:
                    structure_rectangle.top = rectangles.bottom
                    self.crash['up'] = True

                self.position[1] = structure_rectangle.y
        if gestore[0] > 0:
            self.invert = False
        if gestore[0] < 0:
            self.invert = True

        self.final_gestore = gestore

        self.quickness[1] = min(5, self.quickness[1] + 0.1)

        if self.crash['down'] or self.crash['up']:
            self.quickness[1] = 0
        self.gestore.version()

    def translate(self, surface, counteract=(0, 0)):
        """handling the flip part (output the appropriate flipped image)"""
        surface.blit(pygame.transform.flip(self.gestore.image(), self.invert, False), (self.position[0] - counteract[0] + self.movement_counter[0], self.position[1] - counteract[1] + self.movement_counter[1]))


class Rival(PhysMath):

    """
    controls the enemies that walk and shot at the character
    """

    def __init__(self, maingame, position, bigness):
        super().__init__(maingame, 'enemy', position, bigness)

        self.stroll = 0

    def version(self, maps, gestore=(0, 0)):
        """controls walking and solid ground and what they do when not walking"""
        if self.stroll:
            if maps.firm_examine((self.rectangle().centerx + (-7 if self.invert else 7), self.position[1] + 23)):
                if self.crash['right'] or self.crash['left']:
                    self.invert = not self.invert
                else:
                    gestore = (gestore[0] - 0.5 if self.invert else 0.5, gestore[1])
            else:
                self.invert = not self.invert
            self.stroll = max(0, self.stroll - 1)

            if not self.stroll:
                distance = (self.main.character.position[0] - self.position[0], self.main.character.position[1] - self.position[1])
                if abs(distance[1]) < 16:
                    if self.invert and distance[0] < 0:
                        self.main.sounds['shoot'].play()
                        self.main.missiles.append([[self.rectangle().centerx - 7, self.rectangle().centery], -1.5, 0])
                        """controls the spark from the gun when looking left"""
                        for i in range(4):
                            self.main.speck.append(Speck(self.main.missiles[-1][0], random.random() - 0.5 + math.pi, 2 + random.random()))
                    if not self.invert and distance[0] > 0:
                        self.main.sounds['shoot'].play()
                        self.main.missiles.append([[self.rectangle().centerx + 7, self.rectangle().centery], 1.5, 0])
                        """spark from the gun when looking right"""
                        for i in range(4):
                            self.main.speck.append(Speck(self.main.missiles[-1][0], random.random() - 0.5, 2 + random.random()))

        elif random.random() < 0.01:
            self.stroll = random.randint(30, 120)

        super().version(maps, gestore=gestore)

        if gestore[0] != 0:
            # you are moving
            self.calibrate_activity('run')
        else:
            self.calibrate_activity('idle')

        if abs(self.main.character.rushing) >= 50:
            if self.rectangle().colliderect(self.main.character.rectangle()):
                self.main.window_sway = max(16, self.main.window_sway)
                self.main.sounds['hit'].play()
                """to find out if they collide when player is dashing and adds sparks"""
                for i in range(30):
                    slant = random.random() * math.pi * 2
                    pace = random.random() * 5
                    self.main.speck.append(Speck(self.rectangle().center, slant, 2 + random.random()))
                    self.main.fragments.append(Fragment(self.main, 'particle', self.rectangle().center, quickness=[math.cos(slant + math.pi) * pace * 0.5, math.sin(slant + math.pi) * pace * 0.5], structure=random.randint(0, 7)))

                self.main.speck.append(Speck(self.rectangle().center, 0, 5 + random.random()))
                self.main.speck.append(Speck(self.rectangle().center, math.pi, 5 + random.random()))

                return True

    def translate(self, surface, counteract=(0, 0)):
        """allows the gun to flip with the enemy"""
        super().translate(surface, counteract=counteract)

        if self.invert:
            surface.blit(pygame.transform.flip(self.main.aids['gun'], True, False), (self.rectangle().centerx - 4 - self.main.aids['gun'].get_width() - counteract[0], self.rectangle().centery - counteract[1]))
        else:
            surface.blit(self.main.aids['gun'], (self.rectangle().centerx + 4 - counteract[0], self.rectangle().centery - counteract[1]))


class Character(PhysMath):

    """
    controls the characters movements and applies pysics to the character
    """

    def __init__(self, maingame, position, bigness):
        super().__init__(maingame, 'player', position, bigness)
        self.in_air = 0
        self.leaps = 1

        self.barrier_slip = False
        self.rushing = 0

    def version(self, maps, gestore=(0, 0)):
        """controls the jumping, wall slide, and dashing (with pysics)"""
        super().version(maps, gestore=gestore)

        self.in_air += 1

        if self.in_air > 120:
            if not self.main.deceased:
                self.main.window_sway = max(16, self.main.window_sway)

            self.main.deceased += 1

        if self.crash['down']:
            self.in_air = 0
            self.leaps = 1

        self.barrier_slip = False
        if (self.crash['right'] or self.crash['left']) and self.in_air > 4:
            self.barrier_slip = True
            self.quickness[1] = min(self.quickness[1], 0.5)
            if self.crash['right']:
                self.invert = False
            else:
                self.invert = True
            self.calibrate_activity('wall_slide')

        if not self.barrier_slip:
            if self.in_air > 4:
                self.calibrate_activity('jump')
            elif gestore[0] != 0:
                self.calibrate_activity('run')
            else:
                self.calibrate_activity('idle')

        if abs(self.rushing) in (60, 50):
            """at the start or end of dash have 20 particles that fade out or appear"""
            for i in range(20):
                slant = random.random() * math.pi * 2
                pace = random.random() * 0.5 + 0.5

                c_quickness = [math.cos(slant) * pace, math.sin(slant) * pace]
                self.main.fragments.append(Fragment(self.main, 'particle', self.rectangle().center, quickness=c_quickness, structure=random.randint(0, 7)))

        if self.rushing > 0:
            self.rushing = max(0, self.rushing - 1)
        if self.rushing < 0:
            self.rushing = min(0, self.rushing + 1)

        if abs(self.rushing) > 50:
            self.quickness[0] = abs(self.rushing) / self.rushing * 8
            if abs(self.rushing) == 51:
                self.quickness[0] *= 0.1
            # dashing on the x-axis only
            c_quickness = [abs(self.rushing) / self.rushing * random.random() * 3, 0]
            self.main.fragments.append(Fragment(self.main, 'particle', self.rectangle().center, quickness=c_quickness, structure=random.randint(0, 7)))

        if self.quickness[0] > 0:
            self.quickness[0] = max(self.quickness[0] - 0.1, 0)
        else:
            self.quickness[0] = min(self.quickness[0] + 0.1, 0)

    def translate(self, surface, counteract=(0, 0)):
        """adding in the particles and their slow recede when the character is not dashing"""
        if abs(self.rushing) <= 50:
            super().translate(surface, counteract=counteract)

    def leap(self):
        """allow the character to jump only once. also allow a wall slide."""
        if self.barrier_slip:
            if self.invert and self.final_gestore[0] < 0:
                self.quickness[0] = 3.5
                self.quickness[1] = -2.5
                self.in_air = 5
                self.leaps = max(0, self.leaps - 1)
                return True
            elif not self.invert and self.final_gestore[0] > 0:
                self.quickness[0] = -3.5
                self.quickness[1] = -2.5
                self.in_air = 5
                self.leaps = max(0, self.leaps - 1)
                return True

        elif self.leaps:
            self.quickness[1] = -3
            self.leaps -= 1
            self.in_air = 5

    def rush(self):
        """allows the character to dash left or right and adds the sound"""
        if not self.rushing:
            self.main.sounds['dash'].play()
            if self.invert:
                self.rushing = -60
            else:
                self.rushing = 60



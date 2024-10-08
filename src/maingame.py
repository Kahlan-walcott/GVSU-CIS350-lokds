import sys
import json
import pygame
import os

IMAGE_TRACK = 'data/images/'

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('A Dog\'s Journey')

        self.size_of_tile = 16
        self.map = {}
        self.decimalTiles = []
        self.window = pygame.display.set_mode((640, 480))
        self.exhibit = pygame.Surface((320, 240))
        self.time = pygame.time.Clock()
        self.positionChange = [False, False]

        self.roll = [0, 0]
        self.dog_pos = [50, 50]
        self.dog_size = (8, 15)
        self.dog_velocity = [0, 0]
        self.air_time = 0
        self.dog_action = 'idle'
        self.dog_flip = False
        self.dog_animation = self.load_sprite('idle', 6)

        self.aids = {
            'decor': self.add_graphics('tiles/decor'),
            'grass': self.add_graphics('tiles/grass'),
            'large_decor': self.add_graphics('tiles/large_decor'),
            'stone': self.add_graphics('tiles/stone'),
            'player': self.add_graphic('entities/player.png'),
            'background': self.add_graphic('background.png'),
            'clouds': self.add_graphics('clouds'),
            'water': self.add_graphics('tiles/water'),
        }

        self.load('level1.json')

    def add_graphic(self, file):
        graphic = pygame.image.load(IMAGE_TRACK + file).convert()
        graphic.set_colorkey((0, 0, 0))
        return graphic

    def add_graphics(self, file):
        graphics = []
        try:
            for graphic in sorted(os.listdir(IMAGE_TRACK + file)):
                graphics.append(self.add_graphic(file + '/' + graphic))
        except pygame.error:
            graphics.append(self.add_graphic('tiles/water/0.png'))
            if os.path.exists(IMAGE_TRACK + file):
                print(f"File exists: {IMAGE_TRACK + file}")
        return graphics

    def load_sprite(self, action, img_dur=5):
        images = self.add_graphics(f'entities/player/{action}')
        return {'images': images, 'img_dur': img_dur, 'frame': 0, 'loop': True}

    def load(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
            self.map = data['tilemap']
            self.size_of_tile = data['tile_size']
            self.decimalTiles = data['offgrid']

    def neighbor_tiles(self, position):
        neighbor_tiles = []
        location = (int(position[0] // self.size_of_tile), int(position[1] // self.size_of_tile))
        TILES_AROUND = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
        for distance in TILES_AROUND:
            locationCheck = str(location[0] + distance[0]) + ';' + str(location[1] + distance[1])
            if locationCheck in self.map:
                neighbor_tiles.append(self.map[locationCheck])
        return neighbor_tiles

    def phys_collide(self, position):
        rectangles = []
        for tile in self.neighbor_tiles(position):
            if tile['type'] in {'grass', 'stone'}:
                rectangles.append(
                    pygame.Rect(tile['pos'][0] * self.size_of_tile, tile['pos'][1] * self.size_of_tile,
                                self.size_of_tile, self.size_of_tile))
        return rectangles

    def blit_on(self, window, distance=(0, 0)):
        for tile in self.decimalTiles:
            window.blit(self.aids[tile['type']][tile['variant']],
                        (tile['pos'][0] - distance[0], tile['pos'][1] - distance[1]))

        for x in range(distance[0] // self.size_of_tile, (distance[0] + window.get_width()) // self.size_of_tile + 1):
            for y in range(distance[1] // self.size_of_tile, (distance[1] + window.get_height()) // self.size_of_tile + 1):
                location = str(x) + ';' + str(y)
                if location in self.map:
                    tile = self.map[location]
                    window.blit(self.aids[tile['type']][tile['variant']], (
                        tile['pos'][0] * self.size_of_tile - distance[0], tile['pos'][1] * self.size_of_tile - distance[1]))

    def update_dog(self):
        move_speed = 1
        self.dog_pos[0] += self.dog_velocity[0] * move_speed
        entity_rect = pygame.Rect(self.dog_pos[0], self.dog_pos[1], *self.dog_size)

        for rect in self.phys_collide(self.dog_pos):
            if entity_rect.colliderect(rect):
                if self.dog_velocity[0] > 0:
                    entity_rect.right = rect.left
                    self.dog_pos[0] = entity_rect.x
                elif self.dog_velocity[0] < 0:
                    entity_rect.left = rect.right
                    self.dog_pos[0] = entity_rect.x

        self.dog_pos[1] += self.dog_velocity[1] * move_speed
        entity_rect.topleft = (self.dog_pos[0], self.dog_pos[1])

        collided_with_ground = False
        for rect in self.phys_collide(self.dog_pos):
            if entity_rect.colliderect(rect):
                if self.dog_velocity[1] > 0:
                    entity_rect.bottom = rect.top
                    self.dog_pos[1] = entity_rect.y
                    self.dog_velocity[1] = 0
                    collided_with_ground = True
                elif self.dog_velocity[1] < 0:
                    entity_rect.top = rect.bottom
                    self.dog_pos[1] = entity_rect.y

        self.dog_flip = self.dog_velocity[0] < 0

        if not collided_with_ground:
            self.dog_velocity[1] = min(3, self.dog_velocity[1] + 0.1)

        if collided_with_ground:
            self.air_time = 0
        else:
            self.air_time += 1

        if self.air_time > 4:
            self.dog_action = 'jump'
        elif self.dog_velocity[0] != 0:
            self.dog_action = 'run'
        else:
            self.dog_action = 'idle'

        self.update_dog_animation()

    def update_dog_animation(self):
        if self.dog_action != self.dog_action:
            self.dog_animation = self.load_sprite(self.dog_action)
            self.dog_action = self.dog_action

        self.dog_animation['frame'] = (self.dog_animation['frame'] + 1) % (self.dog_animation['img_dur'] * len(self.dog_animation['images']))

    def blit_dog(self, surf, distance=(0, 0)):
        image = self.dog_animation['images'][self.dog_animation['frame'] // self.dog_animation['img_dur']]
        flipped_image = pygame.transform.flip(image, self.dog_flip, False)
        surf.blit(flipped_image, (self.dog_pos[0] - distance[0], self.dog_pos[1] - distance[1]))

    def play(self):
        while True:
            self.exhibit.blit(self.aids['background'], (0, 0))
            self.roll[0] += (self.dog_pos[0] - self.exhibit.get_width() / 2 - self.roll[0]) / 30
            self.roll[1] += (self.dog_pos[1] - self.exhibit.get_height() / 2 - self.roll[1]) / 30
            blitOn_roll = (int(self.roll[0]), int(self.roll[1]))

            self.blit_on(self.exhibit, distance=blitOn_roll)
            self.update_dog()
            self.blit_dog(self.exhibit, distance=blitOn_roll)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.dog_velocity[0] = -1
                    if event.key == pygame.K_RIGHT:
                        self.dog_velocity[0] = 1
                    if event.key == pygame.K_UP:
                        self.dog_velocity[1] = -2
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.dog_velocity[0] = 0

            self.window.blit(pygame.transform.scale(self.exhibit, self.window.get_size()), (0, 0))
            pygame.display.update()
            self.time.tick(60)

Game().play()
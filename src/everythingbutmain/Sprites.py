import pygame
import os

BASE_IMG_PATH = 'data/images/'

class Avatar:
    def __init__(self, maingame, avatar_type, position, size):
        self.maingame = maingame
        self.avatar_type = avatar_type
        self.position = list(position)
        self.size = size
        self.avatar_velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        self.gesture = ''
        self.distance = (-3, -3)
        self.rotate = False
        self.set_gesture('thing')
        self.airBourne = 0

    def rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def set_gesture(self, gesture):
        if gesture != self.gesture:
            self.gesture = gesture
            self.animation = self.maingame.resources[self.avatar_type + '/' + self.gesture].duplicate()

    def update_avatar(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        frame_movement = (movement[0] + self.avatar_velocity[0], movement[1] + self.avatar_velocity[1])
        self.position[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in self.maingame.physics_rectangles(self.position):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.position[0] = entity_rect.x

        self.position[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in self.maingame.physics_rectangles(self.position):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.position[1] = entity_rect.y

        if movement[0] > 0:
            self.rotate = False
        if movement[0] < 0:
            self.rotate = True
        else:
            self.avatar_velocity[1] = min(4, self.avatar_velocity[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.avatar_velocity[1] = 0
        self.airBourne += 1
        if self.collisions['down']:
            self.airBourne = 0

        if self.airBourne > 4:
            self.set_gesture('thing')
        elif movement[0] != 0:
            self.set_gesture('run')
        else:
            self.set_gesture('thing')

        self.animation.advance()

    def render(self, surf, offset=(0, 0)):
        surf.blit(pygame.transform.flip(self.animation.current_image(), self.rotate, False),
                  (self.position[0] - offset[0] + self.distance[0], self.position[1] - offset[1] + self.distance[1]))

class AnimationSequence:
    def __init__(self, frames, duration_per_frame=5, is_looping=True):
        self.frames = frames
        self.is_looping = is_looping
        self.duration_per_frame = duration_per_frame
        self.is_complete = False
        self.current_frame_index = 0

    def duplicate(self):
        return AnimationSequence(self.frames, self.duration_per_frame, self.is_looping)

    def advance(self):
        if self.is_looping:
            self.current_frame_index = (self.current_frame_index + 1) % (self.duration_per_frame * len(self.frames))
        else:
            self.current_frame_index = min(self.current_frame_index + 1, self.duration_per_frame * len(self.frames) - 1)
            if self.current_frame_index >= self.duration_per_frame * len(self.frames) - 1:
                self.is_complete = True

    def current_image(self):
        return self.frames[int(self.current_frame_index / self.duration_per_frame)]




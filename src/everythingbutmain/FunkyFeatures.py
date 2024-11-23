import pygame
import random
from everythingbutmain.Sprites import Avatar
class Artifacts:

    def __init__(self, maingame):
        self.maingame = maingame
        self.not_picked_up = {}
        i = 0
        if self.maingame.currentMap == 'map.json':
            for artifact in maingame.resources['artifacts']:

                random_x = random.randint(0, 400)
                random_y = random.randint(20, 50)
                while self.maingame.physics_rectangles([random_x, random_y]):
                    random_x = random.randint(0, 400)
                    random_y = random.randint(20, 50)
                self.not_picked_up[i] = [artifact, [random_x, random_y]]
                i+=1
        else:
            for artifact in maingame.resources['artifacts']:

                random_x = random.randint(0, 500)
                random_y = random.randint(-9, 50)
                while self.maingame.physics_rectangles([random_x, random_y]):
                    random_x = random.randint(0, 500)
                    random_y = random.randint(-9, 50)
                self.not_picked_up[i] = [artifact, [random_x, random_y]]
                i+=1

        self.canDogMoveOn = False
        self.distance = (-2, -2)


    def drawArtifacts(self, surface, distanceFromCamera=(0, 0)):

        for variantName, imageAndPosition in self.not_picked_up.items():

            surface.blit(imageAndPosition[0], (imageAndPosition[1][0] - distanceFromCamera[0],
                                               imageAndPosition[1][1] - distanceFromCamera[1]))

    def check_collision_with_artifacts(self, player_rect):
        to_remove = []

        for variantName, imageAndPosition in self.not_picked_up.items():
            artifact_position = (imageAndPosition[1][0] + self.distance[0],
                                 imageAndPosition[1][1] + self.distance[1])

            artifact_rect = pygame.Rect(artifact_position[0], artifact_position[1],
                                        imageAndPosition[0].get_width(),
                                        imageAndPosition[0].get_height())

            if player_rect.colliderect(artifact_rect):
                to_remove.append(variantName)

        for item in to_remove:
            del self.not_picked_up[item]
            print('deleted')
        if not self.not_picked_up:
            self.canDogMoveOn = True







class NPCs(Avatar):
    def __init__(self, maingame, avatar_type, position, size, gesture=None):
        super().__init__(maingame, avatar_type, position, size, gesture=None)
        self.maingame = maingame
        self.avatar_type =  avatar_type
        self.position = position
        self.size = size
        self.distance = (-2, -2)
        if self.maingame.currentMap == 'map.json':
            self.position = [419, 86.1]

        else:
            self.position = [742, 6]




    def drawNPC(self, surface, distanceFromCamera=(0, 0)):
        surface.blit(self.avatar[0], (self.position[0] - distanceFromCamera[0],self.position[1] - distanceFromCamera[1]))

    def check_collision_with_NPC(self, player_rect, surface, distanceFromCamera=(0, 0)):


        NPC_position = (self.position[0] + self.distance[0], self.position[1] + self.distance[1])
        NPC_rect = pygame.Rect(NPC_position[0], NPC_position[1], self.size[0], self.size[1])

        if player_rect.colliderect(NPC_rect):


            return True

class NPCMessage:
    def __init__(self, maingame, x_position, y_position, canDogMoveOn, message = ''):
        self.maingame = maingame
        self.x_position = x_position
        self.y_position = y_position
        self.message = message
        self.width = 120
        self.height = 55
        self.color = pygame.Color('pink')
        self.font = pygame.font.SysFont('Arial', 10)
        self.canDogMoveOn = canDogMoveOn
    def setMessage(self, message):
        self.message = message
    def drawMessage(self, screen, distanceFromCamera=(0, 0)):

        rect = pygame.Rect(self.x_position - distanceFromCamera[0],
                           self.y_position - distanceFromCamera[1],
                           self.width, self.height)
        text_surface = self.font.render(self.message, True, pygame.Color('black'))
        text_rect = text_surface.get_rect()
        text_rect.x = rect.x + 5
        text_rect.y = rect.y + 5
        if not self.maingame.artifacts.canDogMoveOn:
            self.setMessage('You have not collected\nall magical bones.\nGo back to collect\nmagical bones.')
        else:
            self.setMessage('You are so close!\nYou have all\nthe magical bones!\nTime to go home!!!')





        pygame.draw.rect(screen, self.color, rect)  # No border width means a solid fill

        # Draw the border outline
        pygame.draw.rect(screen, pygame.Color('black'), rect, 2)

        lines = self.message.splitlines()
        y_offset = 1  # Initial y offset inside the rectangle

        # Render each line separately
        for line in lines:
            text_surface = self.font.render(line, True, pygame.Color('black'))
            text_rect = text_surface.get_rect()
            text_rect.x = rect.x + 5  # Horizontal padding inside the rectangle
            text_rect.y = rect.y + y_offset  # Vertical position for each line
            screen.blit(text_surface, text_rect)

            # Increase the y_offset for the next line to avoid overlap
            y_offset += text_surface.get_height() + 1


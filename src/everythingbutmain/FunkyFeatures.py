import pygame
import random
class Artifacts:

    def __init__(self, maingame):
        self.maingame = maingame
        self.not_picked_up = {}
        i = 0

        for artifact in maingame.resources['artifacts']:

            random_x = random.randint(0, 400)
            random_y = random.randint(20, 50)
            while self.maingame.physics_rectangles([random_x, random_y]):
                random_x = random.randint(0, 400)
                random_y = random.randint(20, 50)
            self.not_picked_up[i] = [artifact, [random_x, random_y]]
            i+=1
        self.canDogMoveOn = False
        self.distance = (-2, -2)


    def drawArtifacts(self, surface, offset=(0, 0)):

        for variantName, imageAndPosition in self.not_picked_up.items():
            surface.blit(imageAndPosition[0], (imageAndPosition[1][0] - offset[0] + self.distance[0], imageAndPosition[1][1] - offset[1] + self.distance[1]))








class NPCs:
    def __init__(self, maingame, avatar):
        self.maingame = maingame
        self.avatar = avatar

        pass

import pygame

from everythingbutmain.Sprites import Avatar


# Colors


class Ghosts:
    def __init__(self, game):
        self.game = game

        # Define ghost properties
        self.ghosts = [
            {'avatar': Avatar(self.game, 'ghost', (100, -35), (16, 16), 'left'), 'x': 100, 'y': -35, 'velocity_x': 2, 'range_x': (80, 240)},
            {'avatar': Avatar(self.game, 'ghost', (150, 50), (16, 16), 'left'), 'x': 150, 'y': 50, 'velocity_x': 2, 'range_x': (100, 260)},
            {'avatar': Avatar(self.game, 'ghost', (300, 70), (16, 16), 'left'), 'x': 300, 'y': 70, 'velocity_x': 2, 'range_x': (200, 400)}
        ]

    def draw_ghosts(self, screen, distanceFromCamera=(0, 0)):
        # Move each ghost horizontally within its defined x-axis range
        for ghost in self.ghosts:
            # Update x position based on velocity
            ghost['x'] += ghost['velocity_x']

            # Reverse direction if the ghost hits its horizontal boundary
            if ghost['x'] <= ghost['range_x'][0] or ghost['x'] >= ghost['range_x'][1]:
                ghost['velocity_x'] = -ghost['velocity_x']

            # Set the ghost's position (x, fixed y)
            ghost['avatar'].position = (ghost['x'], ghost['y'])

            # Draw the ghost at its current position
            screen.blit(
                ghost['avatar'].sprite.current_image(),
                (int(ghost['x'] - distanceFromCamera[0]), int(ghost['y'] - distanceFromCamera[1]))
            )

        pygame.display.flip()

    def check_collision_with_ghosts(self, player_rect):
        # Check for collisions with any ghost
        for ghost in self.ghosts:
            if player_rect.colliderect(ghost['avatar'].rect()):
                return True
        return False



class ObstacleFloat:
    def __init__(self, maingame, floater):
        self.maingame = maingame
        self.floater = maingame.resources[floater]
        # where the tree is is where they start
        self.position = [320.0, 40.0]
        self.pos2 = [174.0, 42.5]


    def update_pos(self, posx, posy):
        # the movement
        x = self.position[0] + 0.2 / 4
        y = self.position[1] - -0.3 / 2
        self.position = [x, y]

        x2 = self.pos2[0] - 0.2 / 4
        y2 = self.pos2[1] - -0.3 / 2
        self.pos2 = [x2, y2]


    def drawObstacle(self, surface, distanceFromCamera=(0, 0)):
        # the leaves for the second tree
        surface.blit(self.floater[0],
                     (self.position[0] + 6 - distanceFromCamera[0] + 20, self.position[1] + 18 - distanceFromCamera[1]))

        surface.blit(self.floater[0],
                     (self.position[0] + 7 - distanceFromCamera[0] - 6, self.position[1] - distanceFromCamera[1]))
        self.update_pos(self.position[0], self.position[1])

        # leaves for the first tree
        surface.blit(self.floater[0],
                     (self.pos2[0] + 6 - distanceFromCamera[0] + 20, self.pos2[1] + 18 - distanceFromCamera[1]))

        surface.blit(self.floater[0],
                     (self.pos2[0] + 9 - distanceFromCamera[0], self.pos2[1] - distanceFromCamera[1]))
        self.update_pos(self.pos2[0], self.pos2[1])

        # once the second leaves hit 100.0 they restart
        if self.position[1] >= 100.0:
            self.position = [320.0, 40.0]
            self.update_pos(self.position[0], self.position[1])
        # once the first leaves hit 90.0 they restart
        if self.pos2[1] >= 90.0:
            self.pos2 = [174.0, 42.5]
            self.update_pos(self.pos2[0], self.pos2[1])
    #get the ghosts



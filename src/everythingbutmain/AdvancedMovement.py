import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_COLOR_1 = (255, 0, 0)
BALL_COLOR_2 = (0, 0, 255)


class Ghosts:
    def __init__(self, game):
        self.game = game
        self.ghost1 = Avatar(self.game, 'ghost', (100, 100), (16, 16), 'left')
        self.ghost2 = Avatar(self.game, 'ghost', (200, 150), (16, 16), 'left')

        # Ghost 1 properties
        self.ghost1_x = 100
        self.ghost1_y = 100
        self.ghost1_velocity_x = 4
        self.ghost1_velocity_y = 3

        # Ghost 2 properties
        self.ghost2_x = 200
        self.ghost2_y = 150
        self.ghost2_velocity_x = 3
        self.ghost2_velocity_y = 4

        # Define grid boundaries
        self.grid_min_x = 0
        self.grid_max_x = 320
        self.grid_min_y = 0
        self.grid_max_y = 240

    def draw_ghosts(self, screen, distanceFromCamera=(0, 0)):
        # Move Ghost 1
        self.ghost1_x += self.ghost1_velocity_x
        self.ghost1_y += self.ghost1_velocity_y

        # Reverse direction if Ghost 1 hits a boundary
        if self.ghost1_x <= self.grid_min_x or self.ghost1_x >= self.grid_max_x - 16:
            self.ghost1_velocity_x = -self.ghost1_velocity_x
        if self.ghost1_y <= self.grid_min_y or self.ghost1_y >= self.grid_max_y - 16:
            self.ghost1_velocity_y = -self.ghost1_velocity_y

        # Update ghost1 position
        self.ghost1.position = (self.ghost1_x, self.ghost1_y)

        # Move Ghost 2
        self.ghost2_x += self.ghost2_velocity_x
        self.ghost2_y += self.ghost2_velocity_y

        # Reverse direction if Ghost 2 hits a boundary
        if self.ghost2_x <= self.grid_min_x or self.ghost2_x >= self.grid_max_x - 16:
            self.ghost2_velocity_x = -self.ghost2_velocity_x
        if self.ghost2_y <= self.grid_min_y or self.ghost2_y >= self.grid_max_y - 16:
            self.ghost2_velocity_y = -self.ghost2_velocity_y

        # Update ghost2 position
        self.ghost2.position = (self.ghost2_x, self.ghost2_y)

        # Draw the ghosts
        screen.blit(self.ghost1.sprite.current_image(),
                    (int(self.ghost1_x - distanceFromCamera[0]), int(self.ghost1_y - distanceFromCamera[1])))
        screen.blit(self.ghost2.sprite.current_image(),
                    (int(self.ghost2_x - distanceFromCamera[0]), int(self.ghost2_y - distanceFromCamera[1])))

        pygame.display.flip()


    def check_collision_with_ghosts(self, player_rect):
         print(self.ghost1.rect(), player_rect)




         if player_rect.colliderect(self.ghost1.rect()):
             print(self.ghost1.rect())
             return True
         if player_rect.colliderect(self.ghost2.rect()):
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



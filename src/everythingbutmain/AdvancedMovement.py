import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_COLOR_1 = (255, 0, 0)
BALL_COLOR_2 = (0, 0, 255)

class Ghosts:
    def __init__(self, game):
        self.game = game
        self.ball_radius = 8

        # Ball 1 properties
        self.ball1_x = 100
        self.ball1_y = 100
        self.ball1_velocity_x = 4
        self.ball1_velocity_y = 3

        # Ball 2 properties
        self.ball2_x = 200
        self.ball2_y = 150
        self.ball2_velocity_x = 3
        self.ball2_velocity_y = 4

        # Define grid boundaries (smaller than screen dimensions of 320x240)
        self.grid_min_x = 20
        self.grid_max_x = 300
        self.grid_min_y = 20
        self.grid_max_y = 220

    def draw_ghosts(self, screen, distanceFromCamera=(0, 0)):
        # Move Ball 1
        self.ball1_x += self.ball1_velocity_x
        self.ball1_y += self.ball1_velocity_y

        # Check collision for Ball 1
        if self.ball1_x - self.ball_radius <= self.grid_min_x or self.ball1_x + self.ball_radius >= self.grid_max_x:
            self.ball1_velocity_x = -self.ball1_velocity_x
        if self.ball1_y - self.ball_radius <= self.grid_min_y or self.ball1_y + self.ball_radius >= self.grid_max_y:
            self.ball1_velocity_y = -self.ball1_velocity_y

        # Move Ball 2
        self.ball2_x += self.ball2_velocity_x
        self.ball2_y += self.ball2_velocity_y

        # Check collision for Ball 2
        if self.ball2_x - self.ball_radius <= self.grid_min_x or self.ball2_x + self.ball_radius >= self.grid_max_x:
            self.ball2_velocity_x = -self.ball2_velocity_x
        if self.ball2_y - self.ball_radius <= self.grid_min_y or self.ball2_y + self.ball_radius >= self.grid_max_y:
            self.ball2_velocity_y = -self.ball2_velocity_y

        # Draw the boundary grid
        #pygame.draw.rect(screen, BLACK, (self.grid_min_x, self.grid_min_y, self.grid_max_x - self.grid_min_x, self.grid_max_y - self.grid_min_y), 2)

        # Draw Ball 1
        pygame.draw.circle(screen, WHITE, (int(self.ball1_x - distanceFromCamera[0]), int(self.ball1_y - distanceFromCamera[1])), self.ball_radius)

        # Draw Ball 2
        pygame.draw.circle(screen, WHITE, (int(self.ball2_x - distanceFromCamera[0]), int(self.ball2_y - distanceFromCamera[1])), self.ball_radius)

        pygame.display.flip()

    # def check_collision_with_ghosts(self, player_rect):
    #
    #
    #
    #     ball1Pos = (self.ball1_x, self.ball1_y)
    #     ball2Pos = (self.ball2_x, self.ball2_y)
    #
    #     ghost1_rect = pygame.Rect(ball1Pos[0], ball1Pos[1],
    #                                     self.GHOSTIMAGE.get_width(),
    #                                     self.GHOSTIMAGE[0].get_height())
    #     ghost2_rect = pygame.Rect(ball1Pos[0], ball1Pos[1],
    #                               self.GHOSTIMAGE.get_width(),
    #                               self.GHOSTIMAGE[0].get_height())
    #
    #     if player_rect.colliderect(ghost1_rect):
    #         return True
    #     if player_rect.colliderect(ghost2_rect):
    #         return True


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




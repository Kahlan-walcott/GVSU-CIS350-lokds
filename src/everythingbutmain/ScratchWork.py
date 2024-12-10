"""
This file holds code for the sine function.
This is one idea we had for the movement of the leaves and the enemies.
"""

import math
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Time variable for the animation
    t = pygame.time.get_ticks() / 2 % 400  # scale and loop time

    # Ball 1 moving from left to right
    x1 = t
    y1 = math.sin(t / 50.0) * 100 + 200     # scale sine wave
    y1 = int(y1)                            # make y1 integer

    # Ball 2 moving from right to left
    x2 = 400 - t                            # opposite direction
    y2 = math.sin(t / 50.0) * 100 + 200     # same sine wave for y
    y2 = int(y2)                            # make y2 integer

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw both circles
    pygame.draw.circle(screen, (255, 255, 255), (int(x1), y1), 20)
    pygame.draw.circle(screen, (255, 0, 0), (int(x2), y2), 20)

    # Update the display
    pygame.display.flip()

pygame.quit()

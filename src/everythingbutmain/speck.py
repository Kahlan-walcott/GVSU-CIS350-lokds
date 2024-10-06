import math

import pygame


class Speck:
    
    """
    Creates a dimond shape based on where the character is moving.
    """
    
    def __init__(self, position, slant, pace):
        self.position = list(position)
        self.slant = slant
        self.pace = pace

    def version(self):
        """controls the shape of the speck when the character dashes and when guns shoot."""
        # x 
        self.position[0] += math.cos(self.slant) * self.pace
        # y
        self.position[1] += math.sin(self.slant) * self.pace

    # is a dimond shape (will slow down and shrink)
        self.pace = max(0, self.pace - 0.1)
        return not self.pace

    def translate(self, surface, counteract=(0, 0)):
        """allows the spark to happen in all directions"""
        translation_spots = [
            # in front of where the spark is going
            # ends are 6 times longer then sides
            (self.position[0] + math.cos(self.slant) * self.pace * 3 - counteract[0], self.position[1] + math.sin(self.slant) * self.pace * 3 - counteract[1]),
            # right or left (don't do opposites next to each other)
            (self.position[0] + math.cos(self.slant + math.pi * 0.5) * self.pace * 3 - counteract[0], self.position[1] + math.sin(self.slant + math.pi * 0.5) * self.pace * 0.5 - counteract[1]),
            # opposite of where the spark is going
            (self.position[0] + math.cos(self.slant + math.pi) * self.pace * 3 - counteract[0], self.position[1] + math.sin(self.slant + math.pi) * self.pace * 3 - counteract[1]),
            (self.position[0] + math.cos(self.slant - math.pi * 0.5) * self.pace * 3 - counteract[0], self.position[1] - math.sin(self.slant + math.pi * 0.5) * self.pace * 0.5 - counteract[1]),
        ]
        
        pygame.draw.polygon(surface, (255, 255, 255), translation_spots)


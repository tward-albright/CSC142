import pygame
from pygame.locals import *

BLUE = (0, 0, 225)


class Raindrop:
    __slots__ = ["x", "y", "radius"]
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1

    def draw(self, window):
        pygame.draw.circle(window, BLUE, (self.x, self.y), self.radius)

    def update(self):
        self.radius += 1

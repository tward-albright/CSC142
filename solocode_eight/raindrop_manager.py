import sys
from random import randint

import pygame
from pygame.locals import *

from raindrop import Raindrop

# 2 - Define constants
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


class RaindropManager:
    RAIN_RATE = 0.01
    MAX_RADIUS = 20

    def __init__(self):
        self.raindrops: list[Raindrop] = []
        self.rate = 0

    def run(self):
        pygame.init()
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # frame-based actions
            if self.rate <= 0:
                self.rate = RaindropManager.RAIN_RATE

                self.raindrops.append(
                    Raindrop(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
                )

            window.fill(LIGHT_BLUE)

            # Draw under here
            # Go backward not to change the indexes of all the raindrops that aren't deleted
            print(len(self.raindrops))
            for i in range(len(self.raindrops))[::-1]:
                self.raindrops[i].update()
                self.raindrops[i].draw(window)

                if self.raindrops[i].radius > RaindropManager.MAX_RADIUS:
                    del self.raindrops[i]

            pygame.display.update()
            self.rate -= clock.get_time() / 1000

            clock.tick(FRAMES_PER_SECOND)

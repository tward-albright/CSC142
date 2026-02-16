# pygame demo 6(b) - using the Ball class, bounce many balls

# 1 - Import packages
import random
import sys

import pygame
from pygame.locals import *

from Ball import *  # bring in the Ball class code

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
last_seconds = 0
score = 0


# 4 - Load assets: image(s), sounds, etc.
def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


# 5 - Initialize variables
ballList = []
for oBall in range(0, N_BALLS):
    # Each time through the loop, create a Ball object
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)  # append the new Ball to the list of Balls

# 6 - Loop forever
while True:
    curr_time = (pygame.time.get_ticks() - start_time) // 1000
    if curr_time == 15:
        for i in ballList:
            del ballList[0]
        break
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for index, ball in enumerate(ballList):
                if ball.ballRect.collidepoint(mouse_pos):
                    score += 1
                    del ballList[index]

    # 8 - Do any "per frame" actions
    for oBall in ballList:
        oBall.update()
        # tell each Ball to update itself
    if curr_time > last_seconds:
        last_seconds = curr_time
        oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
        ballList.append(oBall)

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    for oBall in ballList:
        oBall.draw()  # tell each Ball to draw itself

    draw_text(
        window,
        f"Time: {curr_time}s",
        16,
        32,
        (255, 255, 255),
        48,
    )
    draw_text(window, f"Score: {score}", 16, 64, (255, 255, 255), 48)

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

while True:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_text(
        window,
        f"Final score: {score}",
        WINDOW_WIDTH // 2 - 128,
        WINDOW_HEIGHT // 2 - 32,
        (255, 255, 255),
        48,
    )

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

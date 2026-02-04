# pygame demo 4(c), one image, bounce around the window - with sound

# 1 - Import packages
import random
import sys

import pygame
from pygame.locals import *

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load("images/ball.png")
bounceSound = pygame.mixer.Sound("sounds/boing.wav")
clickSound = pygame.mixer.Sound("sounds/click.mp3")
# pygame.mixer.music.load("sounds/background.mp3")
# pygame.mixer.music.play(-1, 0.0)


# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
start_time = pygame.time.get_ticks()
end_time = 0
player_score = 0


# from Canvas
def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


# get the sign of a number
def sign(n):
    if n >= 0:
        return 1
    return -1


# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if ballRect.collidepoint(mouse_pos):
                player_score += 1
                ballRect.left = random.randint(0, MAX_WIDTH)
                ballRect.top = random.randint(0, MAX_HEIGHT)
                # using sign so that the ball doesn't always go to the bottom-right after clicked
                xSpeed = sign(xSpeed) * (abs(xSpeed) + random.randint(1, 5))
                ySpeed = sign(ySpeed) * (abs(ySpeed) + random.randint(1, 5))
                clickSound.play()

    # 8 - Do any "per frame" actions
    if player_score < 5:
        if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
            xSpeed = -xSpeed  # reverse X direction
            bounceSound.play()

        if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
            ySpeed = -ySpeed  # reverse Y direction
            bounceSound.play()

    if player_score == 5 and end_time == 0:
        end_time = pygame.time.get_ticks() - start_time

    # Update the rectangle of the ball, based on the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    if player_score < 5:
        window.blit(ballImage, ballRect)
    else:
        draw_text(
            window,
            f"Time: {end_time / 1000:.2f}s",
            MAX_WIDTH // 2 - 32,
            MAX_HEIGHT // 2,
            (255, 255, 255),
            48,
        )

    draw_text(window, f"Score: {player_score}", 0, 0, (255, 255, 255), 32)
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

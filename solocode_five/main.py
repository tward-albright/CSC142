#  Demo of pygwidgets capabilities
#
#  4/17  Developed by Irv Kalb

# 1 - Import libraries
import os
import sys

import pygame
import pygwidgets
from pygame.locals import *

# The next line is here just in case you are running from the command line
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 2 - Define constants
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 320
FRAMES_PER_SECOND = 30

# The function and Test class and method below are not required.
# These are only here as a demonstration of how you could use a callback approach to handling events if you want to.


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()  # create a clock object

# 4 - Load assets: image(s), sounds,  etc.
oBackgroundImage = pygwidgets.Image(window, (0, 0), "images/background.jpg")
oDisplayTextTitle = pygwidgets.DisplayText(
    window,
    (0, 20),
    "Temperature Converter",
    fontSize=36,
    width=640,
    textColor=BLACK,
    justified="center",
)

temperature_output = pygwidgets.DisplayText(
    window,
    (100, 150),
    "",
    fontSize=36,
    width=640,
    textColor=BLACK,
    justified="center",
)

temperatureInput = pygwidgets.InputText(
    window, (20, 150), initialFocus=True, textColor=BLACK, fontSize=28
)  # add: , mask='*' for passwords

conversionButton = pygwidgets.TextButton(window, (20, 200), "Convert!")

fahrenheitRadio = pygwidgets.TextRadioButton(
    window, (150, 200), "Default Group", "Convert to Fahrenheit", value=False
)

celciusRadio = pygwidgets.TextRadioButton(
    window, (150, 220), "Default Group", "Convert to Celcius", value=True
)

# 5 - Initialize variables
counter = 0
angle = 0
pct = 100


def convert_temperature(temperature, celcius):
    if celcius:
        return (temperature - 32) / (9 / 5)
    return temperature * (9 / 5) + 32


# 6 - Loop forever
while True:
    # 7 - Check for and handle events

    for event in pygame.event.get():
        # check if the event is the close button
        if event.type == pygame.QUIT:
            # if it is quit, the program
            pygame.quit()
            sys.exit()

        if temperatureInput.handleEvent(event):  # pressed Return or Enter
            theText = temperatureInput.getValue()
            print("The text of oInputTextA is: " + theText)

        if conversionButton.handleEvent(event):  # clicked
            try:
                temperature = int(temperatureInput.getValue().strip())
                is_celcius = celciusRadio.getValue()
                converted_temperature = convert_temperature(temperature, is_celcius)
                temperature_output.setText(
                    f"{converted_temperature:.2f}{'C' if is_celcius else 'F'}"
                )
            except ValueError:  # just do nothing if you can't convert the temperature
                pass

        if fahrenheitRadio.handleEvent(event):  # selected
            print("Radio button text1 was clicked")

        if celciusRadio.handleEvent(event):  # selected
            print("Radio button text2 was clicked")

        if event.type == pygame.KEYDOWN:
            pass

        # If we wanted to keep track of the angle, we could start with:  angle = 0
        # Then for every left arrow:  angle = angle + 5
        # and for every right arrow:  angle = angle - 5
        # Finally, call:  oPythonIcon.rotateTo

    # 8  Do any "per frame" actions
    counter = counter + 1

    # 9 - Clear the window
    oBackgroundImage.draw()

    # 10 - Draw all window elements
    pygame.draw.rect(window, GRAY, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))

    oDisplayTextTitle.draw()
    temperature_output.draw()
    temperatureInput.draw()

    conversionButton.draw()
    fahrenheitRadio.draw()
    celciusRadio.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

#  Game class

import pygwidgets

from card import *
from constants import *
from deck import *


class Game:
    CARD_OFFSET = 110
    CARDS_TOP = 300
    CARDS_LEFT = 75
    NCARDS = 8
    POINTS_CORRECT = 15
    POINTS_INCORRECT = 10

    def __init__(self, window):
        self.window = window
        self.oDeck = Deck(self.window)
        self.score = 100
        self.scoreText = pygwidgets.DisplayText(
            window,
            (450, 164),
            "Score: " + str(self.score),
            fontSize=36,
            textColor=WHITE,
            justified="right",
        )

        self.messageText = pygwidgets.DisplayText(
            window,
            (50, 460),
            "",
            width=900,
            justified="center",
            fontSize=36,
            textColor=WHITE,
        )

        self.loserSound = pygame.mixer.Sound("sounds/loser.wav")
        self.winnerSound = pygame.mixer.Sound("sounds/ding.wav")
        self.cardShuffleSound = pygame.mixer.Sound("sounds/cardShuffle.wav")

        self.cardXPositionsList = []
        thisLeft = Game.CARDS_LEFT
        # Calculate the x positions of all cards, once
        for cardNum in range(Game.NCARDS):
            self.cardXPositionsList.append(thisLeft)
            thisLeft = thisLeft + Game.CARD_OFFSET

        self.reset()  # start a round of the game

    def reset(self):  # this method is called when a new round starts
        self.cardShuffleSound.play()
        self.cardList = []
        self.oDeck.shuffle()
        for cardIndex in range(0, Game.NCARDS):  # deal out cards
            oCard = self.oDeck.getCard()
            self.cardList.append(oCard)
            thisXPosition = self.cardXPositionsList[cardIndex]
            oCard.setLoc((thisXPosition, Game.CARDS_TOP))

        self.showCard(0)
        self.cardNumber = 0
        self.currentCardName, self.currentCardValue = self.getCardNameAndValue(
            self.cardNumber
        )

        self.messageText.setValue(
            "Starting card is "
            + self.currentCardName
            + ". Will the next card be higher or lower?"
        )

    def getCardNameAndValue(self, index):
        oCard = self.cardList[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue

    def showCard(self, index):
        oCard = self.cardList[index]
        oCard.reveal()

    # the player hits
    def hit(self):
        pass

    # the player stands
    def stand(self):
        pass

    def draw(self):
        # Tell each card to draw itself
        for oCard in self.cardList:
            oCard.draw()

        self.scoreText.draw()
        self.messageText.draw()

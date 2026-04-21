#  Game class

import pygame
import pygwidgets

import constants
from deck import CardHolder, Deck


class Game:
    CARD_OFFSET = 110
    CARDS_TOP = 300
    CARDS_LEFT = 25
    NCARDS = 2
    POINTS_CORRECT = 15
    POINTS_INCORRECT = 10

    def __init__(self, window):
        self.window = window
        self.deck = Deck(self.window, rankValueDict=constants.blackJackDict)
        self.player_holder = CardHolder(300, 25)
        self.dealer_holder = CardHolder(125, 25)
        self.standing = False

        self.messageText = pygwidgets.DisplayText(
            window,
            (50, 460),
            "",
            width=900,
            justified="center",
            fontSize=36,
            textColor=constants.WHITE,
        )

        self.playerScore = pygwidgets.DisplayText(
            window,
            (25, 275),
            "",
            width=900,
            justified="left",
            fontSize=24,
            textColor=constants.WHITE,
        )

        self.dealerScore = pygwidgets.DisplayText(
            window,
            (25, 100),
            "",
            width=900,
            justified="left",
            fontSize=24,
            textColor=constants.WHITE,
        )

        self.loserSound = pygame.mixer.Sound("sounds/loser.wav")
        self.winnerSound = pygame.mixer.Sound("sounds/ding.wav")
        self.cardShuffleSound = pygame.mixer.Sound("sounds/cardShuffle.wav")

        self.player_card_positions = []
        self.dealer_car_positions = []

        self.reset()  # start a round of the game

    def reset(self):  # this method is called when a new round starts
        self.standing = False
        self.cardShuffleSound.play()
        self.player_holder.cards = []
        self.dealer_holder.cards = []
        self.player_holder.total = 0
        self.dealer_holder.total = 0
        self.deck.shuffle()
        for cardIndex in range(0, Game.NCARDS):  # deal out cards
            self.draw_card(self.player_holder)

        self.showCard(0)
        self.cardNumber = 0
        self.currentCardName, self.currentCardValue = self.getCardNameAndValue(
            self.cardNumber
        )

        self.messageText.setValue(
            f"Starting card is {self.currentCardName}. Hit or stand?"
        )
        self.playerScore.setValue(f"Player Score: {self.player_holder.total}")
        self.dealerScore.setValue(f"Dealer Score: {self.dealer_holder.total}")

    def getCardNameAndValue(self, index):
        oCard = self.player_holder.cards[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue

    def showCard(self, index):
        oCard = self.player_holder.cards[index]
        oCard.reveal()

    def draw_card(self, location: CardHolder):
        card = self.deck.getCard()
        self.currentCardName = card.cardName
        location.cards.append(card)
        xpos = location.card_left + Game.CARD_OFFSET * (len(location.cards) - 1)
        card.setLoc((xpos, location.card_top))
        card.reveal()
        location.total += card.getValue()
        print(location.total)

        self.playerScore.setValue(f"Player Score: {self.player_holder.total}")

    # the player hits
    def hit(self):
        self.draw_card(self.player_holder)

        self.messageText.setValue(
            f"Drawn card is {self.currentCardName}. Hit or stand?"
        )

        if self.player_holder.total > 21:
            print("Busted!")
            self.messageText.setValue("Player Busted!")
            self.standing = True

    # the player stands
    def stand(self):
        self.standing = True
        while (
            self.dealer_holder.total < 17
            and self.dealer_holder.total < self.player_holder.total
        ):
            self.draw_card(self.dealer_holder)
            self.dealerScore.setValue(f"Dealer Score: {self.dealer_holder.total}")

        if self.dealer_holder.total < self.player_holder.total:
            self.messageText.setValue("Dealer Wins!")
        else:
            self.messageText.setValue("Player Wins!")

    def draw(self):
        # Tell each card to draw itself
        for oCard in self.player_holder.cards:
            oCard.draw()

        for card in self.dealer_holder.cards:
            card.draw()

        self.messageText.draw()
        self.playerScore.draw()
        self.dealerScore.draw()

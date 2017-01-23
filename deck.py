import random
from card import Card


class Deck():
    """
    Represents a card deck
    """

    def __init__(self):
        """
        Initialize deck with 52 Cards
        """
        self.cards = []
        self.resetDeck()
        self.value = 0

    def shuffle(self):
        """
        Shuffle card deck
        """
        random.shuffle(self.cards)

    def __str__(self):
        """
        overrider str to print all cards in the deck
        """
        return "\n".join(str(x) for x in self.cards)

    def takeCard(self):
        """
        Takes bottom card
        """
        return self.cards.pop()

    def addCard(self, card):
        """
        Adds card to deck
        """
        self.cards.append(card)

    def resetDeck(self):
        """
        Resets deck to original state
        """
        self.cards = []
        for suit in range(4):
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

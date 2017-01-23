#!/usr/bin/env python3
"""
classes for card deck
"""
import random
from card import Card


class Hand():
    """
    Represents a hand holding cards
    """

    def __init__(self):
        self.cards = []

    def takeCard(self, deck):
        """
        Takes card from a deck
        """
        self.cards.append(deck.takeCard())

    def playCard(self, index):
        """
        Play a card
        """
        return self.cars.pop(index)

    def __str__(self):
        """
        Override str to show cards
        """
        return ", ".join(str(x) for x in self.cards)

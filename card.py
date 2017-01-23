class Card():
    """
    Represents card in a deck
    """

    names = [None, "ass", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knackt", "Dam", "Kung"]
    suits = ["Hjarter", "Spader", "Klover", "Ruter"]

    def __init__(self, value, suit):
        """
        Value = 1-13
        suit = 0-3
        """
        self.value = value
        self.suit = suit

    def __str__(self):
        """
        Override str to return card name and suit
        """
        return "{} {}".format(Card.suits[self.suit], Card.names[self.value])

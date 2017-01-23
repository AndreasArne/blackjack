from hand import Hand
from deck import Deck

class BlackJack():

    def __init__(self):
        self.players = []
        self.deck = Deck()

    def gameloop(self, deck):
        pass
        # while(1):
            # for nr, player in enumerate(self.players):


    def deal(self):
        for nr, player in enumerate(self.players):
            player.takeCard(self.deck)
            print("{} has cards: {}".format(("Dealer" if nr == 0 else "Player {}".format(nr+1)), player))

    def createPlayers(self):
        """
        Add players and dealer
        """
        nr = input("Number of players: ")
        try:
            for x in range(int(nr)+1):
                self.players.append(Hand())
        except:
            print("Type an int!")

    def init(self):
        self.createPlayers()
        self.deck.shuffle()


if __name__ == "__main__":
    bj = BlackJack()
    bj.init()
    bj.deal()
    bj.deal()

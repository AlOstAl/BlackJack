from random import shuffle
from const import PRINTED, SUITS, RANKS


class Card:
    def __init__(self, suit, rank, picture, points):
        self.suit = suit
        self.rank = rank
        self.picture = picture
        self.point = points

    def __str__(self):
        if self.rank.isdigit():
            rank = self.rank
        else:
            rank = self.rank[0].upper()
        message = rank + self.picture
        # message = rank + self.picture + "Points:" + str(self.point)
        return message


class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        shuffle(self.cards)

    @staticmethod
    def generate_deck():
        cards = []
        for suit in SUITS:
            suit = suit
            for rank in RANKS:
                rank = rank
                if rank == 'ace':
                    points = 11
                elif rank.isdigit():
                    points = int(rank)
                else:
                    points = 10
                picture = PRINTED.get(suit)
                c = Card(suit=suit, rank=rank, picture=picture, points=points)
                cards.append(c)
        return cards

    def get_card(self):
        return self.cards.pop()

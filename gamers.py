import abc
import random
from const import MAX_BET, NAME
from abc import ABC


class AbcGamer(abc.ABC):

    def __init__(self):
        self.name = None
        self.cards = []
        self.bet = 0
        self.full_points = 0
        self.money = 100

    def __str__(self):
        # message = f'Bet: {str(self.bet)} Points {str(self.full_points)}'
        pass

    def take_card(self, card):
        self.cards.append(card)
        self.full_points += card.point

    def get_name(self):
        pass

    def make_bet(self):
        pass


class Player(AbcGamer):
    def __init__(self):
        super().__init__()
        self.name = 'You'

    def __str__(self):
        message = f"You have next cards: ({', '.join([str(x) for x in [*self.cards]])}) " \
                  f"Points: {str(self.full_points)}."
        return message

    def make_bet(self):
        bet = int(input(f'Place your bet (max bet is {MAX_BET}): '))
        # to do check for correct input
        self.bet = bet
        self.money -= self.bet
        print('Your bet is: ', self.bet)


class Bot(AbcGamer):
    def __init__(self):
        super().__init__()

    def __str__(self):
        message = f"{self.name} has next cards: ({', '.join([str(x) for x in [*self.cards]])}) " \
                  f"Points: {str(self.full_points)}."
        return message

    def make_bet(self):
        self.bet = random.randint(1, MAX_BET)
        self.money -= self.bet
        print(f'{self.name}`s bet is: {self.bet}')

    def get_name(self):
        self.name = NAME.pop(random.randint(0, len(NAME)-1))


class Dealer(AbcGamer):
    def __init__(self):
        super().__init__()

    def __str__(self):
        message = f"Dealer`s cards: ({','.join([str(x) for x in [*self.cards]])}) " \
                  f"Points: {str(self.full_points)}."
        return message

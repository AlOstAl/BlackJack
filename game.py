from gamers import Player, Bot, Dealer
from cards import Card, Deck
import random


class Game:
    def __init__(self):
        self.gamers = []
        self.dealer = Dealer()
        self.deck = Deck()
        self.max_bet = 10

    def add_gamers(self, count_of_bot):
        # add bot
        for _ in range(count_of_bot):
            b = Bot()
            b.get_name()
            b.make_bet()
            self.gamers.append(b)
        # add human
        p = Player()
        p.make_bet()
        self.gamers.append(p)
        # print(self.gamers)

    def first_deal(self):
        # deal two cards from the deck to each player in gamers
        for gamer in self.gamers:
            for _ in range(2):
                card = self.deck.get_card()
                gamer.take_card(card)
                # print(card)
            print(gamer)
        # and one card to the dealer
        card = self.deck.get_card()
        self.dealer.take_card(card)
        print(self.dealer)
        return True

    @staticmethod
    def check_points(gamer):
        if gamer.full_points > 21:
            return True
        else:
            return False

    def taking_cards(self):
        for gamer in self.gamers:
            if isinstance(gamer, Bot):
                while gamer.full_points < 17:
                    card = self.deck.get_card()
                    gamer.take_card(card)
                    if self.check_points(gamer):
                        print(f'{gamer} BUST!')
            elif isinstance(gamer, Player):
                while True:
                    asc = input('Do you want to take a card? (y/n)')
                    if asc == 'y' or asc == 'Y':
                        card = self.deck.get_card()
                        gamer.take_card(card)
                        if self.check_points(gamer):
                            print(f'{gamer} You BUST!')
                            break
                    elif asc == 'n' or asc == 'N':
                        break
                    print(gamer)
        return True

    def play_dealer(self):
        while self.dealer.full_points < 17:
            card = self.deck.get_card()
            self.dealer.take_card(card)
        # print(f'Dealer`s points are: {self.dealer.full_points}')
        print(self.dealer)

    def determine_winner(self):
        print('*** The final list is as follows: ***')
        if self.dealer.full_points > 21:
            print('The dealer bust! All players in game are win!')
            for gamer in self.gamers:
                if not self.check_points(gamer):
                    gamer.money += gamer.bet * 2
                    print(f'{gamer} {gamer.name} WINS {gamer.bet * 2} coins.')
                else:
                    print(f'{gamer} {gamer.name} BUST!')
        else:
            for gamer in self.gamers:
                if not self.check_points(gamer):
                    if gamer.full_points > self.dealer.full_points:
                        gamer.money += gamer.bet * 2
                        print(f'{gamer} {gamer.name} WINS {gamer.bet * 2} coins.')
                    elif gamer.full_points == self.dealer.full_points:
                        gamer.money += gamer.bet
                        print(f'{gamer} {gamer.name} WINS {gamer.bet} coins.')
                    else:
                        print(f'{gamer} {gamer.name} losts this game.')
                else:
                    print(f'{gamer} {gamer.name} BUST!')

    def start_game(self):
        while True:
            # start game
            choice = input('Start game: (y/n) ')
            if choice == 'y' or choice == 'Y':
                # check new game or continue
                if len(self.gamers) == 0:
                    print('*** Start a new game ***')
                    count_of_bot = int(input('count of bots: '))
                    self.add_gamers(count_of_bot)
                    d = Deck()
                else:
                    print('\n*** Continue the game ***')
                    for gamer in self.gamers:
                        print(f'{gamer.name} continue game:')
                        gamer.cards = []
                        gamer.make_bet()
                        gamer.full_points = 0
                    self.dealer.cards = []
                    self.dealer.full_points = 0
                print('\n*** first deal ***')
                self.first_deal()
                print('\n*** taking cards ***')
                self.taking_cards()
                print('\n*** play with dealer ***')
                self.play_dealer()
                self.determine_winner()
            elif choice == 'n' or choice == 'N':
                break

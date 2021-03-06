"""
Module:
player_class.py

This is the Player class implementation.
A Player object:
1. Has a name and holds a given number of cards.
2. __str__() dunder: returns player name and number of cards he owns.
3. __len__() dunder: easy return of how many cards the palyer owns.
4. get_cards(...) method: allows the player to add cards in his hands.
5. deal_cards(at_war=Flase) method: allows player to deal cards on the table,
one card of players are not at war and five cards otherwise.
6. shuffle() method: to be used in case players are stuck in an infinite war
session, player will shuffle his cards.
"""


import random


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    # dunder method to print Player
    def __str__(self):
        player_info = ''
        player_info += "{}, has {} cards!".format(self.name, len(self.cards))
        return player_info

    # some users may use a dunder to see how many cards a Player has
    def __len__(self):
        return len(self.cards)

    # method to receive Card objects
    def get_cards(self, cards):
        # check if there is one card to receive or a list of them
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)
        return self.cards

    # method to deal card(s), by default we assume that players are at war
    def deal_cards(self, at_war=False):
        if not at_war:
            return self.cards.pop(0)
        else:
            return [self.cards.pop(0) for card in range(5)]

    # method to shuffle player cards, trying to get out of infinite loops
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

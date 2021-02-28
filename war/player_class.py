"""
Module:
player_class.py

This is the Player class implementation.
A Player object:
1. Is initialized with a name and 26 cards (half of a Deck)
2. Will have a method to receive one or more Card objects
3. Will have a method to deal down one or more Card objects
4. A dunder method to print the Player name, his cards and number of cards
"""

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    # dunder method to print player object
    def __str__(self):
        player_info = ''
        player_info += "{}, I have {} cards!".format(self.name, len(self.cards))
        # we may not want to see the cards of the player
        # for card in self.cards:
        #     player_info += (card.__str__() + '\n')
        return player_info

    # method to receive Card objects
    def get_cards(self, cards):
        # check if there is one card to receive or a list of them
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)
        return self.cards

"""
Module:
player_class.py

This is the Player class implementation.
A Player object:
1. Is initialized with a name and 26 cards (half of a Deck)
2. Will have a method to receive one or more Card objects
3. Will have a method to deal down one or more Card objects
4. A dunder method to print the Player name and number of cards
5. A dunder method to print how many cards the Player has
"""

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    # dunder method to print player object
    def __str__(self):
        player_info = ''
        player_info += "{}, has {} cards!".format(self.name, len(self.cards))
        return player_info

    # dunder to get the number of cards of this Player
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

    # method to deal card(s)
    def deal_cards(self, at_war=False):
        try:
            if not at_war:
                return self.cards.pop(0)
            else:
                return [self.cards.pop(0) for card in range(10)]
        except IndexError:
            print("{} has no cards!".format(self.name))

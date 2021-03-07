"""
Module:
deck_class.py

This is the Deck class implementation.
A Deck object will have:
1. 52 unique Card objects.
2. __str__() dunder: returns how many cards the Deck contains, then returns the
'str' information of each card contained.
3. __len__() dunder: easy return of how many cards are in this deck.
4. shuffle() method: shuffle the deck of cards.
5. deal_card() method: draw one card from he deck (and give it to a player).
"""


# dealing with this crazy import error during pytest
# no idea whi is happening, but seems that pytest re-bases HOME to first folder
# upwards that doesn't contain __init__(), this messes up the trivial import here.
try:
    from card_class import Card
except ImportError:
    from war.card_class import Card

import random


class Deck:
    def __init__(self):
        self.cards = []  # holds 52 cards
        self.suits = ["Clubs", "Hearts", "Diamond", "Spades"]
        self.ranks = {
            "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
            "Nine": 9, "Ten": 10, "Ace": 11, "Jack": 12, "Queen": 13, "King": 14
        }

        # fill Deck object with 52 cards
        for suit in self.suits:
            for rank, value in self.ranks.items():
                self.cards.append(Card(suit, rank, value))

    # dunder method to print this deck
    def __str__(self):
        deck_info = "There are {} cards in this deck:".format(len(self.cards))
        for card in self.cards:
            deck_info += '\n' + card.__str__()
        return deck_info

    # some users may use a dunder to get the deck dimension
    def __len__(self):
        return len(self.cards)

    # method to shuffle the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    # method to deal cards from this deck
    def deal_card(self):
        return self.cards.pop()

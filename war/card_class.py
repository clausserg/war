"""
Module:
card_class.py

This is the Card class implementation.
A Card object:
1. Will have a suit, rank and value.
2. __str__() dunder: returns information about the card object, i.e. card's rank,
suit, and value.
"""


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    #  dunder to print tis card infor
    def __str__(self):
        return "{} of {}, worth {} points."\
                .format(self.rank, self.suit, self.value)

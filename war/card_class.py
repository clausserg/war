"""
Module:
card_class.py

This is class implementation for a Card object
"""


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    #  dunder to print tis card infor
    def __str__(self):
        return "{} of {}, worth {} points.".format(self.rank, self.suit, self.value)

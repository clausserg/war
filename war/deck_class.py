"""
Module:
deck_class.py

This is the Deck class implementation.
A Deck object created, will have:
1. 52 unique Card objects with: suite, rank, value attributes
2. A a print dunder method to print cards in this Deck
3. A len dunder method to get the #cards in the Deck
3. A method that deals one card from the Deck, from position 0
"""


from card_class import Card
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

    # dunder method to get how many cards are in this Deck object
    def __len__(self):
        return len(self.cards)

    # method to shuffle the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    # method to deal cards from this deck
    def deal_card(self):
        if len(self.cards):
            return self.cards.pop()
        else:
            return "Sorry, this deck has no cards!"

"""
Module:
war.py

War card game written for fun while following the 'Complete Python Developer Certification Course' by Imtiaz Ahmad, on Udemy.
This is the main module of the War cards game, contains the game logic.
"""

from card_class import Card
from deck_class import Deck
from player_class import Player


if __name__ == "__main__":
    deck = Deck()
    # shuffle the deck of cards
    deck.shuffle()

    player_one = Player("Claudiu")
    player_two = Player("Flori")

    # deal cards to players from the deck
    while len(deck):
        player_one.get_cards(deck.deal_card())
        player_two.get_cards(deck.deal_card())

    print(player_one)
    print(player_two)

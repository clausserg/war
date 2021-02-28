"""
Module:
war.py

War card game written for fun while following the 'Complete Python Developer Certification Course' by Imtiaz Ahmad, on Udemy.
This is the main module of the War cards game, contains the game logic.
"""

from card_class import Card
from deck_class import Deck
from player_class import Player
from table_class import Table


if __name__ == "__main__":
    # create Deck object and shuffle it
    deck = Deck()
    deck.shuffle()

    # create players
    player_one = Player("Claudiu")
    player_two = Player("Flori")

    # create the gaming table
    table = Table(player_one.name, player_two.name)

    # deal cards to players from the deck
    while len(deck):
        player_one.get_cards(deck.deal_card())
        player_two.get_cards(deck.deal_card())

    card_down = player_one.deal_cards(1)
    table.get_cards(player_one.name, card_down)

    print(table)

    a = table.return_cards()
    player_two.get_cards(a)

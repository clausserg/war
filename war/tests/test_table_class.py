"""
This is module: test_deck_class.py

Unit and regression test for: deck_class.py
"""


from war.table_class import Table
from war.deck_class import Deck
from war.player_class import Player


def test_isinstance_deck():
    """Testing if a created object is instance of the Table class"""

    table = Table("Flori", "Claudiu")
    assert isinstance(table, Table) == True


def test_dunder_deck():
    """Testing the __str__ dunder of a Table object"""

    # create Deck without shuffling it to keep track of cards
    my_deck = Deck()
    # create players and game table
    player_one = Player("Flo")
    player_two = Player("Tom")
    my_table = Table("Flo", "Tom")

    # share cards to players
    while len(my_deck):
        player_one.get_cards(my_deck.deal_card())
        player_two.get_cards(my_deck.deal_card())

    # get cards from the players
    my_table.get_cards(player_one.name, player_one.deal_cards(at_war=True))
    my_table.get_cards(player_two.name, player_two.deal_cards(at_war=True))

    assert my_table.__str__() == \
            "Flo's last card down is Six of Spades, worth 6 points.\n" + \
            "Tom's last card down is Five of Spades, worth 5 points.\n" and \
            len(player_one) == 21 and len(player_two) == 21

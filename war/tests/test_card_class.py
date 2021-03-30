"""
This is module: test_card_class.py

Unit and regression test for: card_class.py
"""


from war.card_class import Card


def test_card_class():
    """Testing the print dunder of a Card object"""

    my_card = Card("Clubs", "Three", 3)
    assert my_card.__str__() == "Three of Clubs, worth 3 points."

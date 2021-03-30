"""
This is module: test_deck_class.py

Unit and regression test for: deck_class.py
"""


from war.deck_class import Deck


def test_isinstance_deck():
    """Testing if a created objects is instance of the Deck class"""

    my_deck = Deck()
    assert isinstance(my_deck, Deck) == True


def test_print_deck():
    """Testing the __str__ dunder of a Deck object"""

    my_deck = Deck()
    assert "King of Spades, worth 14 points." in my_deck.__str__() and \
    "Queen of Hearts, worth 13 points." in my_deck.__str__()


def test_shuffle_deck():
    """Testing the shuffle() method of a Deck object"""

    my_deck = Deck()
    my_deck_shuffled = Deck()
    my_deck_shuffled.shuffle()
    assert my_deck.__str__() != my_deck_shuffled.__str__()


def test_len1_deck():
    """Testing the __len__ dunder of a Deck object"""

    my_deck_one = Deck()
    my_deck_two = Deck()
    my_deck_one.shuffle()
    my_deck_two.shuffle()
    assert my_deck_one.__len__() == 52 and my_deck_two.__len__() == 52


def test_dealcard_deck():
    """Testing the __len__ dunder of a Deck object"""

    my_deck = Deck()
    card_one = my_deck.deal_card()
    card_two = my_deck.deal_card()
    assert my_deck.__len__() == 50 and \
    card_one.__str__() == "King of Spades, worth 14 points." and \
    card_two.__str__() == "Queen of Spades, worth 13 points."

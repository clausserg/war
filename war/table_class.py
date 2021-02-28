"""
Module:
table_class.py

This is the Table class implementation:
1. Will hold cards dealt down by two players
2. Will have a method to receive one or more Card objects from each player
3. Will have a method to deal cards to the winning Player
4. A dunder method to print detail of the table
5. A method returning the winning Player who gets the cards on table
"""


class Table:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

        # store cards on table from each player
        self.cards = {
            self.player_one: [],
            self.player_two: []
        }

    # dunder method to print Table important details
    def __str__(self):
        out_info = "{} and {} is playing!\n"\
                    .format(self.player_one, self.player_two)

        for player in [self.player_one, self.player_two]:
            if len(self.cards[player]):
                out_info += "{}'s last card down is {}\n"\
                            .format(player, self.cards[player][-1].__str__())
            else:
                out_info += "{} has no cards down.\n".format(player)
        return out_info

    # method to receive and store Card objects from Player
    def get_cards(self, player, cards):
        # check if there is one Card to receive or a list of them
        if isinstance(cards, list):
            self.cards[player].extend(cards)
        else:
            self.cards[player].append(cards)

    # method to return all cards on the table
    def return_cards(self):
        all_cards = []
        for player in [self.player_one, self.player_two]:
            while len(self.cards[player]):
                all_cards.append(self.cards[player].pop())
        return all_cards  # this always returns a list of Card objects

    # see who wins the cards on table
    def winning(self):
        if self.cards[self.player_one][-1].value > self.cards[self.player_two][-1].value:
            return self.player_one
        elif self.cards[self.player_two][-1].value > self.cards[self.player_one][-1].value:
            return self.player_two
        else:
            return "AT WAR!"

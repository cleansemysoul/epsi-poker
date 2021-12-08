import model.deck as d
import model.hand as ha
import model.human as hu
import model.player as p
import model.ai as a
import model.table as t
import logging
logging.basicConfig(level=logging.INFO)


class SoloGame:
    """ represent solo game """

    HUMAN_NAME = 'Vous'
    AI_NAME = ['Magali', 'Mégane', 'Enora']
    NB_CARDS_HAND = 2
    NB_CARDS_TABLE = 3

    def __init__(self, seed: int):

        # new deck
        self.__deck = d.Deck()
        self.__deck.shuffle_cards(seed)

        # add human player
        human = hu.Human(self.HUMAN_NAME)
        self.add_hand(human)
        self.__human_player = human

        # add artificial intelligence players
        def add(name):
            ai = a.Ai(name)
            self.add_hand(ai)
            return ai
        self.__ai_players = list(map(add, self.AI_NAME))

        # add table
        table = t.Table()
        self.__deck.move_cards_to_table(table, self.NB_CARDS_TABLE)
        self.__table = table

    # a getter function
    @property
    def human_player(self):
        return self.__human_player

    # a getter function
    @property
    def ai_players(self):
        return self.__ai_players

    # a getter function
    @property
    def table(self):
        return self.__table

    def add_hand(self, player: p.Player):
        hand = ha.Hand()
        hand.sort_cards()
        self.__deck.move_cards_to_hand(hand, self.NB_CARDS_HAND)
        player.hand = hand

import model.deck as d
import model.hand as ha
import model.human as hu
import model.player as p
import model.ai as a
import logging
logging.basicConfig(level=logging.INFO)


class SoloGame:
    """ represent solo game """

    HUMAN_NAME = 'Vous'
    AI_NAME = ['Magali', 'Mégane', 'Enora']
    NB_CARDS = 5

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

    # a getter function
    @property
    def human_player(self):
        return self.__human_player

    # a getter function
    @property
    def ai_players(self):
        return self.__ai_players

    def add_hand(self, player: p.Player):
        hand = ha.Hand()
        hand.sort_cards()
        self.__deck.move_cards(hand, self.NB_CARDS)
        player.hand = hand

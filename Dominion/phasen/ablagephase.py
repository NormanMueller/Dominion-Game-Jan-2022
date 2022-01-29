from Dominion.karten_definieren.karten_class import *
from random import shuffle
import collections
from itertools import chain
from Dominion.spieler import spieler
from typing import List, Dict


class ablage_phase:
    def __init__(self, spieler, karten_dict):
        self.spieler = spieler
        self.karten_dict = karten_dict

    def discard_hand_cards(self):
        for handkarte in self.spieler.hand_cards:
            self.spieler.discard_pile.append(handkarte)

    def restore_action_card_pile(self):
        self.spieler.played_action_card_pile = []

    def start_ablage_phase(self):
        self.discard_hand_cards()
        self.restore_action_card_pile()

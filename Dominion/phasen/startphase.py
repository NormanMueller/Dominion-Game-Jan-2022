from Dominion.karten import karten_dict, karten 
from random import shuffle
import collections
from itertools import chain
from Dominion.spieler import spieler

class start_phase():
    
    def __init__(self,spieler,karten_dict):
        self.spieler = spieler
        self.karten_dict = karten_dict
    
    def start_nachziehphase(self):
    
        self.spieler.hand_cards = []
        self.spieler.hand_cards.append(self.spieler.draw_cards(5))
        self.spieler.hand_cards = self.spieler.filter_none_type_cards(self.spieler.hand_cards)
        self.spieler.number_actions= 1
        self.spieler.number_buys= 1

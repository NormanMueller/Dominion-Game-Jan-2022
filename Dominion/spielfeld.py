from Dominion.karten_definieren.karten_class import *
from typing import List, Dict


class spielfeld:
    def __init__(self, karten=karten_dict):
        self.spielfeld_attr = karten

x = spielfeld()

from Dominion.karten_definieren.karten_class import *


class spielfeld:
    def __init__(self, karten=karten_dict):
        self.spielfeld_attr = karten

x = spielfeld()

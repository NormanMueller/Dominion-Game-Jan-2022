from random import shuffle
import collections
from Dominion.spieler import spieler
from Dominion.spielzug import spielzug, spielfeld
from Dominion.spiel import Spiel
from Dominion.karten_definieren.karten_class import *
from typing import List, Dict


spieler1 = spieler(
    card_deck=karten(
        karten=[markt, markt, markt, markt, hexe, markt, hexe, hexe, hexe, hexe]
    ),
    karten_dict=karten_dict,
    name="Nico",
)
spieler2 = spieler(
    card_deck=karten(
        karten=[markt, markt, markt, markt, hexe, markt, markt, markt, hexe, markt]
    ),
    karten_dict=karten_dict,
    name="Norman",
)
x = Spiel(spieler1, spieler2)
x.start_spiel()

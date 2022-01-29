from random import shuffle
import collections
from Dominion.spieler import spieler
from Dominion.spielzug import spielzug, spielfeld
from Dominion.spiel import Spiel
from Dominion.karten_definieren.karten_class import *


spieler1 = spieler(
    card_deck=karten(
        karten=[dorf, dorf, dorf, dorf, miliz, dorf, miliz, miliz, miliz, miliz]
    ),
    karten_dict=karten_dict,
    name="Nico",
)
spieler2 = spieler(
    card_deck=karten(
        karten=[dorf, dorf, dorf, dorf, miliz, dorf, dorf, dorf, miliz, dorf]
    ),
    karten_dict=karten_dict,
    name="Norman",
)
x = Spiel(spieler1, spieler2)
x.start_spiel()

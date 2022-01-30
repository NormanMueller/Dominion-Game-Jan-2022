from random import shuffle
import collections
from Dominion.spieler import spieler
from Dominion.spielzug import spielzug, spielfeld
from Dominion.spiel import Spiel
from Dominion.karten_definieren.karten_class import *
from typing import List, Dict, Type, Generic, Any,Union


spieler1 = spieler(
    card_deck=karten(
        karten=[kupfer, moneylander, moneylander, kupfer, moneylander, moneylander, vasall, dorf, dorf, chapel]
    ),
    karten_dict=karten_dict,
    name="Nico",
)
spieler2 = spieler(
    card_deck=karten(
        karten=[laboratory, dorf, vasall, dorf, laboratory, vasall, festival, vasall, vasall, chapel]
    ),
    karten_dict=karten_dict,
    name="Norman",
)
x = Spiel(spieler1, spieler2)
x.start_spiel()

from random import shuffle
import collections
from Dominion.spieler import spieler
from Dominion.spielzug import spielzug, spielfeld
from Dominion.spiel import Spiel
from Dominion.karten_definieren.karten_class import *
from typing import List, Dict, Type, Generic, Any,Union


spieler1 = spieler(
    card_deck=karten(
        karten=[festival, festival, council_room, festival, festival, council_room, council_room, council_room, festival, festival]
    ),
    karten_dict=karten_dict,
    name="Nico",
)
spieler2 = spieler(
    card_deck=karten(
        karten=[laboratory, dorf, vasall, council_room, laboratory, vasall, festival, vasall, vasall, chapel]
    ),
    karten_dict=karten_dict,
    name="Norman",
)
x = Spiel(spieler1, spieler2)
x.start_spiel()

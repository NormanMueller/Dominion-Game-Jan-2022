from random import shuffle
import collections
from Dominion.karten_definieren.karten_class import *
from Dominion.spieler import spieler
from Dominion.phasen.aktionsphase import action_phase
from Dominion.phasen.kaufphase import kauf_phase
from Dominion.phasen.startphase import start_phase
from Dominion.phasen.ablagephase import ablage_phase
from Dominion.spielfeld import spielfeld
from typing import List, Dict, Type, Generic, Any,Union


class spielzug:

    # TODO

    def __init__(
        self,
        spieler: Type[spieler] =spieler() ,
        no_turn_spieler: Type[spieler] = spieler(),
        spielfeld: Type[spielfeld] = spielfeld(),
        karten_dict: Dict[str,any] = karten_dict,
        karten_dict_class: Type[karten]  = karten_dict_class,
    ):

        self.spieler = spieler
        self.no_turn_spieler = no_turn_spieler
        self.spielfeld = spielfeld
        self.karten_dict = karten_dict
        self.karten_dict_class = karten_dict_class
        self.spieler_karten = self.spieler.card_deck
        self.card__drawing_phase = start_phase(self.spieler, self.karten_dict)
        self.action_phase = action_phase(
            self.spieler, self.no_turn_spieler, self.karten_dict, self.karten_dict_class
        )
        self.kaufphase = kauf_phase(self.spieler, self.spielfeld)
        self.ablagephase = ablage_phase(self.spieler, self.karten_dict)

    def start_spielzug(self):

        print(f"Der Zug von {self.spieler.name} beginnt")
        if self.spieler.turn_counter == 0:
            self.card__drawing_phase.start_nachziehphase()
        self.action_phase.start_aktionsphase()
        self.kaufphase.start_buying_phase()
        self.ablagephase.start_ablage_phase()
        self.card__drawing_phase.start_nachziehphase()
        self.spieler.turn_counter += 1
        print(
            f"Fertig , das war Zug {self.spieler.turn_counter} von  {self.spieler.name} "
        )

#from xmlrpc.client import Boolean
from Dominion.karten_definieren.karten_class import *
from random import shuffle
import collections
from itertools import chain
from Dominion.spieler import spieler
from typing import List, Dict, Type, Generic, Any, Union


class action_phase:
    """Eine action_card kann die folgenden Effekte haben :
    Der Spieler zieht eine karte, Der Spieler bekommt Zusatzaktionen , Der Spieler bekommt Zusatzgeld"""

    def __init__(
        self,
        spieler: Type[spieler],
        no_turn_spieler: Type[spieler],
        karten_dict: Dict[str, any],
        karten_dict_class: Type[karten],
    ):
        self.spieler = spieler
        self.no_turn_spieler = no_turn_spieler
        self.karten_dict = karten_dict
        self.karten_dict_class = karten_dict_class

    def get_card_type(self, card_type):
        card_type = self.karten_dict.get(card_type).get("type")
        return card_type

    def permitted_action_card(self, choose_card: str, hand_cards):
        if choose_card in hand_cards:
            return True

    def reduce_remaining_actions(self):
        self.spieler.number_actions = self.spieler.number_actions - 1

    def action_phase_infos(self):
        return f" hand_cards: {self.spieler.hand_cards} \n number_actions: {self.spieler.number_actions} \n Geld : {self.spieler.geld}"

    def add_to_played_action_card_pile(self, card: Type[karten]) ->None:
        self.spieler.played_action_card_pile.append(card)

    def remove_played_card_from_hand(self, choose_card: str) ->None:
        self.spieler.hand_cards.remove(choose_card)

    def check_discard_effects_on_other_player(self, choose_card) ->bool:
        discard_effect = self.karten_dict.get(choose_card).get("discard_effect")
        if discard_effect >= 1:
            return True

    def stop_action_phase(self):
        def playable_action_cards(self, hand_cards) ->bool:
            aktion_cards = 0
            for hand_card in hand_cards:
                if self.get_card_type(hand_card) == "action_card":
                    aktion_cards += 1
            return aktion_cards

        if (
            self.spieler.number_actions < 1
            or playable_action_cards(self, self.spieler.hand_cards) <= 0
        ):
            return True
        else:
            return False

    def start_aktionsphase(self) ->None:
        print(self.action_phase_infos())
        while True:

            if self.stop_action_phase() == False:
                choose_card = input(
                    "Welche Karte möchtest du spielen? /ansonsten tippe nein"
                )
                if (
                    self.permitted_action_card(choose_card, self.spieler.hand_cards)
                    == True
                ):
                    self.reduce_remaining_actions()
                    setattr(
                        getattr(karten_dict_class, choose_card),
                        "spieler_x",
                        self.spieler,
                    )
                    setattr(
                        getattr(karten_dict_class, choose_card),
                        "no_turn_spieler_x",
                        self.no_turn_spieler,
                    )

                    try:
                        getattr(karten_dict_class, choose_card).func1()
                    except:
                        pass

                    try:
                        getattr(karten_dict_class, choose_card).func2()
                    except:
                        pass

                    try:
                        getattr(karten_dict_class, choose_card).func3()
                    except:
                        pass

                    self.spieler = getattr(
                        karten_dict_class, choose_card
                    ).return_spieler()
                    self.no_turn_spieler = getattr(
                        karten_dict_class, choose_card
                    ).return_no_turn_spieler()

                    self.remove_played_card_from_hand(choose_card)
                    self.add_to_played_action_card_pile(choose_card)
                    print(self.action_phase_infos())

                elif choose_card == "":
                    break
                elif choose_card not in self.spieler.hand_cards:
                    print("Feler wähle bitte eine neue Karte")

            else:
                break

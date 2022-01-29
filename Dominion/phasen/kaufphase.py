from Dominion.karten_definieren.karten_class import *
from random import shuffle
import collections
from itertools import chain
from Dominion.spieler import spieler
from Dominion.spielfeld import spielfeld
from typing import List, Dict, Type, Generic, Any, Union


class kauf_phase:
    def __init__(self, spieler: Type[spieler], spielfeld: Type[spielfeld]):

        self.spieler = spieler
        self.karten_dict = karten_dict
        self.spielfeld = spielfeld

    def update_spielfeld(self, new_karte: str) ->None:
        anzahl = self.spielfeld.get(new_karte).get("anzahl")
        self.spielfeld.get(new_karte).update({"anzahl": anzahl - 1})

    def buy_card_from_stock(self, new_karte: str) ->None:
        self.spieler.append_card_to_card_deck(new_karte)
        self.spieler.append_card_to_discard_pile(new_karte)

    def available_money_for_buy(self, money_list: List[int]) ->int:
        money = sum(money_list)
        return money

    def get_card_price(self, auswahl_karte: str) ->int:
        card_cost = self.karten_dict.get(auswahl_karte).get("kosten")
        return card_cost

    def evaluate_buy_process(self, available_money: int, auswahl_karte: str, number_buys: int) ->bool:
        def check_correct_user_input(self, auswahl_karte):
            if auswahl_karte in self.spielfeld.keys():
                return True
            else:
                return False

        def valid_money_and_buys(self, auswahl_karte: str) -> bool:
            if (
                available_money >= self.get_card_price(auswahl_karte)
                and number_buys >= 1
            ):
                return True

        if check_correct_user_input(self, auswahl_karte) == True:
            if valid_money_and_buys(self, auswahl_karte) == True:
                return True

    def buy_phase_infos(self, money: int) :
        return f"  Geld : {money} , number buys : {self.spieler.number_buys}"

    def start_buying_phase(self) -> None:

        while self.spieler.number_buys >= 1:

            self.spieler.money_counting()
            available_money = self.available_money_for_buy(self.spieler.geld)
            print(self.buy_phase_infos(available_money), self.spieler.hand_cards)
            auswahl_karte = input("welche Karte willst du kaufen ?")

            if (
                self.evaluate_buy_process(
                    available_money, auswahl_karte, self.spieler.number_buys
                )
                == True
            ):
                self.buy_card_from_stock(auswahl_karte)
                self.update_spielfeld(auswahl_karte)
                self.spieler.number_buys += -1
                available_money = available_money - self.get_card_price(auswahl_karte)
            else:
                print("Kauf nicht möglich geld oder aktionen fehlen")

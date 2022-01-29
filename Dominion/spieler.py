from Dominion.karten_definieren.karten_class import *
from random import shuffle
import collections
from itertools import chain
from typing import List, Dict, Type, Generic, Any, Union


class spieler:
    def __init__(
        self,
        card_deck: Type[karten] = karten(["kupfer"] * 7 + ["anwesen"] * 3),
        karten_dict: Dict[str, any] = "",
        name: str = "Hans",
    ):
        self.card_deck = card_deck.card_names
        self.number_actions = 1
        self.number_buys = 1
        self.karten_dict = karten_dict
        self.hand_cards = []
        self.discard_pile = []
        self.draw_pile = card_deck.card_names
        self.draw_pile_generator = self.initialize_draw_pile_generator()
        self.played_action_card_pile = []
        self.geld = []
        self.name = name
        self.phase_zug = ""
        self.turn_counter = 0

    def shuffle_discard_pile(self, cards):
        cards = [[card] for card in cards]
        shuffle(cards)
        return cards

    def reset_draw_pile_to_empty(self):
        self.draw_pile = []

    def reset_discard_pile_to_empty(self):
        self.discard_pile = []

    def update_draw_pile(self):

        if self.discard_pile == []:
            cards = self.draw_pile
        else:
            cards = self.discard_pile

        self.reset_draw_pile_to_empty()
        shuffled_cards = self.shuffle_discard_pile(cards)
        deck = []
        for i in shuffled_cards:
            self.draw_pile.extend(i)
        self.reset_discard_pile_to_empty()

    def initialize_draw_pile_generator(self):
        self.update_draw_pile()
        for i in [[i] for i in self.draw_pile]:
            yield i

    def filter_none_type_cards(self, hand_cards):
        hand_cards = [i for i in hand_cards if i is not None]
        return hand_cards

    def draw_cards(self, anz):
        def draw_single_card(draw_pile):
            return next(draw_pile)

        if len(self.hand_cards) + len(self.played_action_card_pile) <= len(
            self.card_deck
        ):
            for i in range(anz):
                try:
                    self.hand_cards.append(
                        draw_single_card(self.draw_pile_generator)[0]
                    )
                except StopIteration:  # new shuffle needed!!!
                    self.draw_pile_generator = self.initialize_draw_pile_generator()
                    self.hand_cards.append(
                        draw_single_card(self.draw_pile_generator)[0]
                    )

    def money_counting(self):
        def reset_money_account(self):
            self.geld = []

        def get_card_type(self, card_type):
            card_type = self.karten_dict.get(card_type).get("type")
            return card_type

        def evaluate_money(self, card):
            hand_money = self.karten_dict.get(card).get("extra_money")
            self.geld.append(hand_money)

        def evaluate_hand_cards(self):

            for hand_card in self.hand_cards:
                card_type = get_card_type(self, hand_card)
                if card_type == "money_card":
                    evaluate_money(self, hand_card)

        def evaluate_action_cards(self):
            for action_card in self.played_action_card_pile:
                evaluate_money(self, action_card)

        reset_money_account(self)
        evaluate_hand_cards(self)
        evaluate_action_cards(self)

    def count_card_deck(self, card_deck):
        card_count = collections.Counter(card_deck)
        return card_count

    def append_card_to_card_deck(self, new_karte):
        self.card_deck.append(new_karte)

    def append_card_to_discard_pile(self, new_karte):
        self.discard_pile.append(new_karte)

    def get_victory_points_player(self, card_deck):
        def get_victory_points_card(self, card):
            victory_points = self.karten_dict.get(card).get("siegpunkte")
            return victory_points

        player_cards = card_deck
        player_victory_points = []
        for card in player_cards:
            player_victory_points.append(get_victory_points_card(self, card))
        return sum(player_victory_points)

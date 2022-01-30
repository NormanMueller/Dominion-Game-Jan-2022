from ast import Break
from typing import List, Dict
from Dominion.karten_definieren.karten_dict import karten_dict


def get_draws_from_action_card(self, karten_dict_class) -> None:
    def draw_cards(self):
        self.spieler_x.draw_cards(self.zusatz_karten)
    draw_cards(self)


def get_action_from_action_card(self, karten_dict_class) -> None:
    def actions(self):
        zusatz_aktionen = self.zusatz_aktionen
        self.spieler_x.number_actions = self.spieler_x.number_actions + zusatz_aktionen
    actions(self)


def get_buys_from_action_card(self, karten_dict_class) -> None:
    def buys(self):
        zusatz_kaufe = self.zusatz_kaufe
        self.spieler_x.self.number_buys = self.spieler_x.self.number_buys + zusatz_kaufe
    buys(self)


def force_other_player_to_discard_hand(self, choose_card, karten_dict_class) -> None:
    self.no_turn_spieler_x.hand_cards.remove(choose_card)


def permitted_action_card(self, choose_card, karten_dict_class) -> bool:
    if choose_card in self.no_turn_spieler_x.hand_cards:
        return True

def permitted_action_card_player(self, choose_card, karten_dict_class) -> bool:
    if choose_card in self.spieler_x.hand_cards:
        return True

def excecute_discard_effects_on_other_player(self, karten_dict_class) -> None:

    for i in range(self.discard_effect):
        while True and len(self.no_turn_spieler_x.hand_cards) > 3:
            print(f"Hand_cards : {self.no_turn_spieler_x.hand_cards}")
            card_to_discard = input("card to discard")
            if permitted_action_card(self, card_to_discard) == True:
                force_other_player_to_discard_hand(self, card_to_discard)
                print("Choose actual Hand Card")
                break


def get_other_player_curse(self, karten_dict_class):
    self.no_turn_spieler_x.append_card_to_discard_pile("curse")
    self.no_turn_spieler_x.append_card_to_card_deck("curse")


def get_money_from_discard_copper(self, karten_dict_class):
    if 'kupfer' in self.spieler_x.hand_cards:
        self.spieler_x.delete_card_permanently('kupfer')
    else :
        print('cant play moneylander')


def trash_treasure_get_new_cost_up_to_3 (self, karten_dict_class):
    choose_card = input("choose card ")
    if permitted_action_card_player(choose_card, karten_dict_class ) == True and karten_dict.get(choose_card).get('type') == 'money_card'  : 
        self.spieler_x.delete_card_permanently(choose_card)
        self.spieler_x.append_card_to_card_deck()
        self.spieler_x.hand_cards.append()


def play_action_card_twice(self, karten_dict_class):
    choose_card = input("choose card ")

    setattr(
        getattr(karten_dict_class, choose_card),
        "spieler_x",
        self.spieler_x,
    )
    
    while True:
        if choose_card in self.spieler_x.hand_cards:
            for i in range(2):
                try: 
                    getattr(karten_dict_class, choose_card).func1(karten_dict_class) 
                except:
                    pass
                try:
                    getattr(karten_dict_class, choose_card).func2(karten_dict_class) 
                except:
                    pass
                try:
                    getattr(karten_dict_class, choose_card).func3(karten_dict_class) 
                except:
                    pass
            break
    self.spieler_x.hand_cards.remove(choose_card)
    self.spieler_x.append_card_to_discard_pile(choose_card)
    

def play_next_action_card_free(self, karten_dict_class):
    
    self.spieler_x.draw_cards(1)
    choose_card = self.spieler_x.hand_cards[len(self.spieler_x.hand_cards)-1]
    print(choose_card, type(choose_card))
    
    if karten_dict.get(choose_card).get('type') == 'action_card' :
        print(f'es wird ausgespielt: {choose_card}')
        setattr(
            getattr(karten_dict_class, choose_card),
            "spieler_x",
            self.spieler_x,
        )

        try: 
            getattr(karten_dict_class, choose_card).func1(karten_dict_class) 
        except:
            pass
        try:
            getattr(karten_dict_class, choose_card).func2(karten_dict_class) 
        except:
            pass
        try:
            getattr(karten_dict_class, choose_card).func3(karten_dict_class) 
        except:
            pass    
        self.spieler_x.hand_cards.remove(choose_card)
        self.spieler_x.append_card_to_discard_pile(choose_card)
    else :
        print(f'es nicht wird ausgespielt: {choose_card}')


def get_card_from_supply_cost4(self, karten_dict_class) -> None:

    while True:
        card = input("Choose card from supply costing up to 4")
        if card in karten_dict:
            self.spieler_x.append_card_to_discard_pile(card)
            self.spieler_x.append_card_to_card_deck(card)
            break


def delete_cards(self, karten_dict_class) -> None:
    for i in range(self.delete_cards):
        while True:
            card = input("Choose card to delete; skip -> empty ").strip()
            if card in self.spieler_x.hand_cards:
                self.spieler_x.delete_card_permanently(card)
                break
            elif not card:
                print("Überspringen ")
                break
            else:
                print("Choose actual Hand Card")

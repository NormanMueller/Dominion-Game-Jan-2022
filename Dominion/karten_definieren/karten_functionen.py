from typing import List, Dict
from Dominion.karten_definieren.karten_dict import karten_dict

def get_draws_from_action_card (self ) -> None: 
   def draw_cards(self):
      self.spieler_x.draw_cards(self.zusatz_karten)  
   draw_cards(self)


def get_action_from_action_card (self)  -> None: 
   def actions(self):
       zusatz_aktionen = self.zusatz_aktionen
       self.spieler_x.number_actions =   self.spieler_x.number_actions  + zusatz_aktionen
   actions(self)

def force_other_player_to_discard_hand(self, choose_card) -> None: 
    self.no_turn_spieler_x.hand_cards.remove(choose_card)

def permitted_action_card (self, choose_card) -> bool: 
    if choose_card in self.no_turn_spieler_x.hand_cards:
        return True   

def excecute_discard_effects_on_other_player(self) -> None: 

    for i in range(self.discard_effect):
        while True  and len(self.no_turn_spieler_x.hand_cards)>3 :
            print(f'Hand_cards : {self.no_turn_spieler_x.hand_cards}')
            card_to_discard = input('card to discard')
            if permitted_action_card(self, card_to_discard) == True:
                force_other_player_to_discard_hand(self, card_to_discard)
                print('Choose actual Hand Card')
                break

def get_other_player_curse(self) :
    self.no_turn_spieler_x.append_card_to_discard_pile('curse')
    self.no_turn_spieler_x.append_card_to_card_deck('curse')

def get_card_from_supply_cost4 (self) -> None: 

    while True: 
        card = input('Choose card from supply costing up to 4')
        if  card in karten_dict:
            self.spieler_x.append_card_to_discard_pile(card)
            self.spieler_x.append_card_to_card_deck(card)
            break

def delete_cards (self) -> None: 
    for i in range(self.delete_cards):
        while True : 
            card = input('Choose card to delete').strip()
            if  card in self.spieler_x.hand_cards:
                self.spieler_x.delete_card_permanently(card)
                break
            elif not card :
                break
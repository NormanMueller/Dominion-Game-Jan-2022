from Dominion.karten import karten_dict, karten 
from random import shuffle
import collections
from itertools import chain
from Dominion.spieler import spieler

class action_phase():
    """ Eine action_card kann die folgenden Effekte haben : 
     Der Spieler zieht eine karte, Der Spieler bekommt Zusatzaktionen , Der Spieler bekommt Zusatzgeld"""
    
    def __init__(self,spieler,karten_dict):
        self.spieler = spieler
        self.karten_dict = karten_dict

    def get_card_type (self, card_type ): 
      card_type = self.karten_dict.get(card_type).get('type')
      return card_type

    def permitted_action_card (self, choose_card ,hand_cards) :
        if choose_card in hand_cards:
            return True
    
    def reduce_remaining_actions(self):
        self.spieler.number_actions= self.spieler.number_actions-1

    def action_phase_infos (self):
        return f' hand_cards: {self.spieler.hand_cards} \n number_actions: {self.spieler.number_actions} \n Geld : {self.spieler.geld}'  

    def add_to_played_action_card_pile(self, card):
        self.spieler.played_action_card_pile.append(card)

    def get_effects_from_action_card (self,choose_card): 

        def draw_cards(self,choose_card):
            anzahl_zusatz_karten = self.karten_dict.get(choose_card).get('zusatz_karten') 
            self.spieler.draw_cards(anzahl_zusatz_karten)
        
        def add_number_actions(self,choose_card):
            anzahl_zusatz_aktionen = self.karten_dict.get(choose_card).get('zusatz_aktionen') 
            self.spieler.number_actions = self.spieler.number_actions+ anzahl_zusatz_aktionen 
       
        draw_cards(self,choose_card)
        add_number_actions(self, choose_card)

    def remove_played_card_from_hand(self, choose_card):
        self.spieler.hand_cards.remove(choose_card)
    
    def stop_action_phase(self):
        
        def playable_action_cards(self, hand_cards): 
            aktion_cards= 0
            for hand_card in hand_cards:
                if self.get_card_type(hand_card) == 'action_card':
                    aktion_cards += 1
            return aktion_cards

        if self.spieler.number_actions < 1 or playable_action_cards(self, self.spieler.hand_cards) <= 0:
            return True
        else :
            return False

    def start_aktionsphase(self):
       
        while True:
            
            print(self.action_phase_infos())
            
            if self.stop_action_phase() == False:
                choose_card = input('Welche Karte möchtest du spielen? /ansonsten tippe nein') 
                if self.permitted_action_card(choose_card, self.spieler.hand_cards) ==True:
                    self.get_effects_from_action_card(choose_card)
                    self.remove_played_card_from_hand(choose_card)
                    self.add_to_played_action_card_pile(choose_card)
                    self.reduce_remaining_actions()
                elif choose_card == '':
                    break
                elif choose_card not in self.spieler.hand_cards:
                    print('Feler wähle bitte eine neue Karte')

            else:
                break
         

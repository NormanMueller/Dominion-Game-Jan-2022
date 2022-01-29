from random import shuffle
import collections
from Dominion.karten_definieren.karten_class import * 
from Dominion.spieler import spieler
from Dominion.spielzug import spielzug
from typing import List, Dict

class Spiel():
    
    def __init__ (self, spieler = spieler(), spieler_2 = spieler(), spielfeld = karten_dict, karten_dict=karten_dict):
      self.spieler = spieler
      self.spieler_2 = spieler_2
      self.spielfeld = spielfeld
      self.karten_dict = karten_dict
      self.spielzug = spielzug()

    
    def start_spiel (self): 
        
        def game_ends_provinz_empty(self):

            if self.spielfeld.get('provinz').get('anzahl') >0 :
                return False
            else :
                return True  
        
        def game_ends_three_piles_empty(self):

            empty_piles = 0
           
            for i in self.spielfeld.keys():
                anzahl = self.spielfeld.get(i).get('anzahl')
                if anzahl == 0 :
                    empty_piles +=1 
            if empty_piles < 3 :
                return False
            else:
                return True

        while game_ends_provinz_empty(self) == False and game_ends_three_piles_empty(self) == False :

            for spieler in [self.spieler, self.spieler_2]:
                if spieler == self.spieler:
                    no_turn_player = self.spieler_2
                else :
                    no_turn_player = self.spieler
                
                spielzug(  spieler, no_turn_player, self.spielfeld , self.karten_dict).start_spielzug()
                player_points = spieler.get_victory_points_player( spieler.card_deck)
                card_count = spieler.count_card_deck( spieler.card_deck)
                print(f'deine Punkte {player_points},  {card_count}')


from Dominion.karten import karten_dict, karten 
from random import shuffle
import collections
from itertools import chain
from Dominion.spieler import spieler  
from Dominion.spielfeld import spielfeld


class kauf_phase():
    
    def __init__(self,spieler, spielfeld ):
        
        self.spieler = spieler
        self.karten_dict = karten_dict 
        self.spielfeld = spielfeld

    def update_spielfeld (self,new_karte):
      anzahl = self.spielfeld.get(new_karte).get('anzahl') 
      self.spielfeld.get(new_karte).update({'anzahl': anzahl-1})
    
    def buy_card_from_stock (self,new_karte):
      self.spieler.append_card_to_card_deck(new_karte)
      self.spieler.append_card_to_discard_pile(new_karte)

    def available_money_for_buy (self, money_list): 
        money = sum(money_list)
        return money

    def get_card_price(self, card):
        card_cost = self.karten_dict.get(card).get('kosten')
        return card_cost

    def evaluate_buy_process(self, money, card_cost, number_buys ):
        if money >= card_cost and number_buys >= 1:
            return True
        else:
            return False
    
    def buy_phase_infos (self, money):
        return f'  Geld : {money}'  

    def start_buying_phase(self):
        
        while self.spieler.number_buys >= 1 :
            
            self.spieler.money_counting()
            money = self.available_money_for_buy(self.spieler.geld)
            print(self.buy_phase_infos(money))
            auswahl_karte =input("welche Karte willst du kaufen ?")    
            card_cost = self.get_card_price(auswahl_karte)
           
            if  self.evaluate_buy_process(money, card_cost ,self.spieler.number_buys) == True:
                self.buy_card_from_stock(auswahl_karte) 
                self.update_spielfeld(auswahl_karte)
                self.spieler.number_buys += -1
                money = money - card_cost
            else :
                print('Kauf nicht möglich geld oder aktionen fehlen')


def get_draws_from_action_card (self ): 
   def draw_cards(self):
      self.spieler.draw_cards(self.zusatz_karten)  
  
   draw_cards(self)


def get_action_from_action_card (self ): 
   def actions(self):
       zusatz_aktionen = self.zusatz_aktionen
       self.spieler.number_actions =   self.spieler.number_actions  + zusatz_aktionen
  
   actions(self)


def excecute_discard_effects_on_other_player(self) :
        
    def force_other_player_to_discard_hand(self, choose_card):
        self.no_turn_spieler.hand_cards.remove(choose_card)
    
    def permitted_action_card (self, choose_card ,hand_cards) :
        if choose_card in hand_cards:
            return True   

    for i in range(self.discard_effect):
        while True :
            print(f'{self.no_turn_spieler.name} du musst Karten ablegen {self.no_turn_spieler.hand_cards}')
            discard_card = input('Welche Karte möchtest du ablegen?')
            if permitted_action_card(discard_card, self.no_turn_spieler.hand_cards) ==True: 
                force_other_player_to_discard_hand(self, discard_card)
                break 


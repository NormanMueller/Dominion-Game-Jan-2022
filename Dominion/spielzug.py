from random import shuffle
import collections
from Dominion.karten import karten_dict, karten 
from Dominion.spieler import spieler
from Dominion.phasen.aktionsphase import action_phase
from Dominion.phasen.kaufphase import kauf_phase
from Dominion.phasen.startphase import start_phase 
from Dominion.phasen.ablagephase import ablage_phase 
from Dominion.spielfeld import spielfeld


class spielzug ():

 # TODO  
  
  def __init__ (self, 
                spieler = spieler(), 
                spielfeld = spielfeld(), 
                karten_dict=karten_dict ):
                
    self.spieler= spieler
    self.spielfeld = spielfeld.spielfeld_attr
    self.karten_dict = karten_dict
    self.spieler_karten = self.spieler.card_deck
    self.card__drawing_phase = start_phase(self.spieler, self.karten_dict)
    self.action_phase = action_phase(self.spieler, self.karten_dict)
    self.kaufphase = kauf_phase(self.spieler,self.spielfeld )
    self.ablagephase = ablage_phase(self.spieler, self.karten_dict)


  def start_spielzug(self):

    print(f'Der Zug von {self.spieler.name} beginnt')
    self.card__drawing_phase.start_nachziehphase()
    self.action_phase.start_aktionsphase()
    self.kaufphase.start_buying_phase()
    self.ablagephase.start_ablage_phase()
    print(f'Fertig , das war Zug  von  {self.spieler.name}')
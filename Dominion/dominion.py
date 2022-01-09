from random import shuffle
import collections
from Dominion.karten import karten_dict, karten 
from Dominion.spieler import spieler
from Dominion.spielzug import spielzug, spielfeld
from Dominion.spiel import Spiel



#if __name__ =="__main__":
spieler1= spieler(karten(['miliz']*7 + ['anwesen']*3) , karten_dict=karten_dict , name='Nico')
spieler2= spieler( karten(['kupfer']*7 + ['anwesen']*3), karten_dict=karten_dict , name='Norman')
x = Spiel(spieler1 , spieler2 )
x.start_spiel()



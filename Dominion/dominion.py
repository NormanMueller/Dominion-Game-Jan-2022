from random import shuffle
import collections
from Dominion.spieler import spieler
from Dominion.spielzug import spielzug, spielfeld
from Dominion.spiel import Spiel
from Dominion.karten_definieren.karten_class import *


spieler1= spieler( card_deck = karten( karten=[gold,gold, gold,gold,schmiede,gold,schmiede,schmiede,schmiede,schmiede])
                , karten_dict=karten_dict , 
                name='Nico')
spieler2= spieler(card_deck =  karten( karten =[ schmiede,dorf, schmiede,dorf,schmiede,dorf,schmiede,dorf,schmiede,dorf])
                , karten_dict=karten_dict , 
                name='Nico')
#spieler2= spieler( karten(['kupfer']*7 + ['anwesen']*3), karten_dict=karten_dict , name='Norman')
x = Spiel(spieler1 , spieler2 )
x.start_spiel()


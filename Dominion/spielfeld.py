from Dominion.karten import karten_dict, karten 

class spielfeld():
   
    def __init__ (self, karten= karten(karten_dict)):
        
        self.spielfeld_attr = karten.karten
        self.spielfeld_namen= karten.karten_definieren





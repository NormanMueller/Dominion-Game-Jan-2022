from types import MethodType
from Dominion.karten_definieren.karten_dict import karten_dict
from Dominion.karten_definieren.karten_functionen import *
import threading
from threading import Thread

### Aktionskarten
####
class action_card:
    def return_spieler(self):
        return self.spieler_x

    def return_no_turn_spieler(self):
        return self.no_turn_spieler_x


# Init Schmiede
schmiede = action_card()
for i, j in karten_dict.get("schmiede").items():
    setattr(schmiede, i, j)
schmiede.func1 = MethodType(get_draws_from_action_card, schmiede)

# Init dorf
dorf = action_card()
for i, j in karten_dict.get("dorf").items():
    setattr(dorf, i, j)

dorf.func1 = MethodType(get_draws_from_action_card, dorf)
dorf.func2 = MethodType(get_action_from_action_card, dorf)

# Init Markt
markt = action_card()
for i, j in karten_dict.get("markt").items():
    setattr(markt, i, j)

# Init Hexe
hexe = action_card()
for i, j in karten_dict.get("hexe").items():
    setattr(hexe, i, j)

# Init Miliz
miliz = action_card()
for i, j in karten_dict.get("miliz").items():
    setattr(miliz, i, j)
miliz.func1 = MethodType(excecute_discard_effects_on_other_player, miliz)

### geldkarten
####


class treasure_card:
    pass


# Init kupfer
kupfer = treasure_card()
for i, j in karten_dict.get("kupfer").items():
    setattr(kupfer, i, j)

# Init silber
silber = treasure_card()
for i, j in karten_dict.get("silber").items():
    setattr(silber, i, j)

# Init gold
gold = treasure_card()
for i, j in karten_dict.get("gold").items():
    setattr(gold, i, j)


### Punktecarten
####


class victory_card:
    pass


# Init anwesen
anwesen = victory_card()
for i, j in karten_dict.get("anwesen").items():
    setattr(anwesen, i, j)

# Init herzogentum
herzogentum = victory_card()
for i, j in karten_dict.get("herzogentum").items():
    setattr(herzogentum, i, j)

# Init provinz
provinz = victory_card()
for i, j in karten_dict.get("provinz").items():
    setattr(provinz, i, j)


class karten:
    def __init__(self, karten):
        self.karten = karten
        self.card_names = []
        self.karten_definieren()

    def karten_definieren(self):
        try:
            for i in self.karten:
                self.card_names.append(i.name)
        except:
            pass


karten_dict_class = karten(
    [kupfer, silber, gold, anwesen, herzogentum, provinz, dorf, schmiede, miliz, markt]
)

for index in range(len(karten_dict_class.karten)):
    setattr(
        karten_dict_class,
        karten_dict_class.card_names[index],
        karten_dict_class.karten[index],
    )

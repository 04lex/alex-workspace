import enum

class AlegeriJoc(enum.Enum):
    Piatra   = 1
    Hartie   = 2
    Foarfeca = 3

alegere_1 = AlegeriJoc.Hartie
alegere_2 = AlegeriJoc(3)

if alegere_1 == alegere_2:
    print("Sunt egale")
else:
    print("Nu sunt egale")


class RezultatJoc(enum.Enum):
    CASTIGATOR = "winner"
    PIERZATOR  = "loser"
    EGALITATE  = "equality"

rezultat = RezultatJoc.CASTIGATOR
print(rezultat.value)
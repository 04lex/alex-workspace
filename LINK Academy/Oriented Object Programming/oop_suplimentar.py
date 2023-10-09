class Locuinta:
    def __init__(self, numeClient: str = None, suprafataUtila: int = 0, discount: float = 0):
        self.__numeClient = numeClient
        self.__suprafataUtila = suprafataUtila
        self.__discount = discount

    def __str__(self):
        return f'Proprietarul {self.__numeClient} ofera spre vanzare locuinta cu suprafata de {self.__suprafataUtila} m2 suprafata utila cu un discount de {self.__discount} '


    def suprafataUtila(self):
        return self.__suprafataUtila

    def getSuprafataUtila(self):
        return f'Suprafata utila: {int(self.__suprafataUtila)} m2'
        

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, newDiscount):
        if newDiscount >= 0:
            self.__discount = newDiscount
        else:
            return

    def __iadd__(self, discount):
        self.__discount += discount

    def __isub__(self, discount):
        self.__discount -= discount


class Apartament(Locuinta):
    def __init__(self, numeClient: str, suprafataUtila: int, discount: float, etaj: int):
        super().__init__(numeClient, suprafataUtila, discount)
        self.etaj = etaj

    def __str__(self):
        return super().__str__() + f'la etajul {self.etaj} intr-un bloc de apartamente.'


class Casa(Locuinta):
    def __init__(self, numeClient: str, suprafataUtila: int, discount: float, suprafataCurte: int, nrEtaje: int, *suprafataEtaje: float):
        super().__init__(numeClient, suprafataUtila, discount)
        self.suprafataCurte = suprafataCurte
        self.nrEtaje = nrEtaje
        self.suprafataEtaje = suprafataEtaje
        self.suprafataEtaje = []

    def setSuprafataEtaje(self, *suprafateNoi):
        for suprafata in suprafateNoi:
            if isinstance(suprafata, float) and suprafata in range (5, 100):
                self.suprafataEtaje.append(suprafata)

    def __str__(self):
        return super().__str__() + f', o curte cu suprafata de {self.suprafataCurte} m2, {self.nrEtaje} etaje, suprafata etajelor fiind {self.suprafataEtaje} m2'



class AgentieImobiliara(Locuinta):
    def __init__(self, numeClient: str = None, suprafataUtila: int = 0, discount: float = 0):
        super().__init__(numeClient, suprafataUtila, discount)
        self.listaLocuinte = []


    def __iadd__(self, locuinta):
        self.listaLocuinte += locuinta

    def adaugaInLista(self, locuinteNoi):
        for locuinta in locuinteNoi:
            if isinstance(locuinta, object):
                self.listaLocuinte.append(locuinta)



    
    


apartamentNord = Apartament('Ion Popescu', 100, 0, 4)
print(apartamentNord)

apartamentNord.discount = 10000
print(apartamentNord)

apartamentNord.discount -= 2000
print(apartamentNord)

print(apartamentNord.getSuprafataUtila())

print("-------------")

casaVest = Casa("Marian Georgescu", 300, 4500.5, 70, 2)
casaVest.setSuprafataEtaje(30.0, 28.0)

print(casaVest)

class Locuinta:
    def __init__(self, numeClient: str, suprafataUtila: int, discount: float):
        self._numeClient = numeClient
        self._suprafataUtila = suprafataUtila
        self._discount = discount

    def __str__(self):
        return f'Proprietarul {self._numeClient} ofera spre vanzare locuinta cu suprafata de {self._suprafataUtila} m2 suprafata utila cu un discount de {self._discount}'


# class Apartament(Locuinta):
#     def __init__(self, numeClient: str, suprafataUtila: int, discount: float, etaj: int):
#         super().__init__(numeClient, suprafataUtila, discount)
#         self.etaj = etaj

#     def __str__(self):
#         return super().__str__() + f'la etajul {self.etaj} intr-un bloc de apartamente.'


# class Casa(Locuinta):
#     def __init__(self, numeClient: str, suprafataUtila: int, discount: float):
#         super().__init__(numeClient, suprafataUtila, discount)
    


# apartamentNord = Apartament('Ionut', 100, 0, 4)
# print(apartamentNord)

test = Locuinta("Ionut", 50, 0.0)
print(test)
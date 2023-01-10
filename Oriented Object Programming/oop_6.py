Definiti clasa Motor continand informatii despre seria motorului, puterea acestuia si numarul de kilometri parcursi.

class Motor(abc.ABC):
    # Overload / Supraincarcare
    def __init__(self, seria:str, puterea:int, kilometraj:int = 0):
        self._seria = seria
        self.__puterea = puterea
        self._kilometraj = kilometraj

    @abc.abstractmethod
    def metodaExemplu(self):
        print("Exemplu")

    def __iadd__(self, km):
        self.kilometraj += km
        return self


    def getSeria(self):
        return self._seria

    @property
    def kilometraj(self):
        return self._kilometraj

    @kilometraj.setter
    def kilometraj(self, km_noi):
        if km_noi >= 0:
            self._kilometraj = km_noi

    @property
    def seria(self):
        return self._seria

    @property
    def puterea(self):
        return self.__puterea

    @puterea.setter
    def puterea(self, noua_valoare):
        print("Setterul puterii este chemat")
        if noua_valoare < self.__puterea * 2:
                return 
        elif noua_valoare < 0:
            return
        self.__puterea = noua_valoare


    def __str__(self):
        return f'Motorul cu seria {self._seria} are {self.__puterea} CP si {self._kilometraj} km '


class MotorBenzina(Motor):
    def __init__(self, seria, puterea, kilometraj, consum):
        super().__init__(seria= "V8", puterea= 30, kilometraj= 0)
        self.consum = consum
    def __str__(self):
        return super().__str__() + f'si {self.consum} l/100km.'

class MotorElectric(Motor):
    def __init__(self, seria, puterea, kilometraj, baterie):
        super().__init__(seria= "EV", puterea= 500, kilometraj= 0)
        self.baterie = baterie
    def __str__(self):
        return super().__str__() + f'si {self.baterie}% baterie.'

    def metodaExemplu(self):
        print("Exemplu")
        

masina_benzina = MotorBenzina("V8", 200, 0, 25)
print(masina_benzina)
print(masina_benzina.getSeria())

masina_electrica = MotorElectric("WBAJXXJJXJ34353", 430, 0, 98)
print(masina_electrica)
print(masina_electrica.getSeria())

masina_benzina.puterea = 300
print(masina_benzina.puterea)

masina_benzina.kilometraj = 120
masina_benzina += 100
print(masina_benzina)



masina_benzina._Motor__puterea = -300
print(masina_benzina._Motor__puterea)




Derivati din aceasta clasa specializarile MotorElectric si MotorBenzina, care aduc in plus informatii privind
bateria (% consumat din baterie la 1km), respectiv consumul de combustibil in litri la suta de kilometri.


masina1 = Motor('qwery', 100, 0)
print(masina1)

masina2 = Motor('qazerty', 100)
print(masina2)


optiuni_vot = ["sarmale", "cozonac", "pomana", "carnati", "piftie"]

class Vot:
    def __init__(self, optiunile):
        self.optiuni = optiunile
        self.a_fost_exercitat = False

    def voteaza(self, optiunea):
        if optiunea in self.optiuni:
            self.a_fost_exercitat = True
            self.optiunea_selectat = optiunea


class BEC:
    def __init__(self, voturi):
        self.voturi = voturi

    def numaraVoturi(self):
        voturi_valide = 0
        numarare_voturi = { }
        for vot in self.voturi:
            if not vot.a_fost_exercitat:
                print('Votul nu este exercitat')
                continue
            else:
                voturi_valide += 1
                
        return f'Avem {voturi_valide} voturi valide cu voturile {numarare_voturi}'



vot1 = Vot(optiuni_vot)
vot2 = Vot(optiuni_vot)
vot3 = Vot(optiuni_vot)
vot4 = Vot(optiuni_vot)


vot1.voteaza("sarmale")
vot2.voteaza("sarmale")
vot3.voteaza("candy")
vot4.voteaza("piftie")

biroul = BEC([vot1, vot2, vot3, vot4])
print(biroul.numaraVoturi())




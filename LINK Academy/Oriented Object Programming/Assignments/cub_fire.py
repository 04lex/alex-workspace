import threading

class Cub:
    def __init__(self, latura):
        self.latura = latura

    def calcul_volum(self):
        volum = self.latura ** 3
        print(f"Volum cub: {self.latura}")

    def calcul_lungime_totala(self):
        lungime_totala = 12 * self.latura
        print(f"Lungime totala laturi: {lungime_totala}")

    
def run_calcul_lungime_totala(cub):
    cub.calcul_lungime_totala()

def run_calcul_volum(cub):
    cub.calcul_volum()

cub1 = Cub(5)
cub2 = Cub(3)

# Thread separat calcul_lungime_totala
thread_calcul_lungime_totala = threading.Thread(target=run_calcul_lungime_totala, args=(cub1,))
thread_calcul_lungime_totala.start()

# Asteptam sa termine thread_calcul_lungime_totala
thread_calcul_lungime_totala.join()

# Thread principal pentru calcul_volum
run_calcul_volum(cub2)
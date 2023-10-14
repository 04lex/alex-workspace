# Verificarea valorii cu TVA a unui produs

TVA = 19
def valoare_cu_TVA(valoarea):
    return valoarea * (1 + TVA/100)

def testeaza_valoare_cu_TVA():
    assert valoare_cu_TVA(100) == 119, "Valoare TVA incorecta"
    assert valoare_cu_TVA(200) == 238, "Valoare TVA incorecta"
    assert valoare_cu_TVA(1000) == 1190, "Valoare TVA incorecta"



if __name__ == "__main__":
    testeaza_valoare_cu_TVA()
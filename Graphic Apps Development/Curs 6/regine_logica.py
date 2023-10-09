# Create your tests here.

def calculeaza_solutii(N):

    # Numarul de regine pe tabla
   
    # Reginele puse pe tabla
    stiva = [0] * N

    print(stiva)

    # Nivelul de regine (cat sunt pe tabla)
    k = 0

    solutii = []

    def este_mutare_valida(k, stiva):
        for i in range(k):
            if (stiva[i] == stiva[k]) or abs(stiva[k]-stiva[i]) == abs(k - i):
                return False
        return True

    while k >= 0:
        if k == N:
            # solutie gasita
            print("Solutia gasita:", stiva)
            solutii.append(stiva.copy())
            k -= 1
        elif stiva[k] < N:
            # verificare valoarea este valida
            stiva[k] += 1
            if este_mutare_valida(k, stiva):
                k += 1
        else:
            # backtracking
            stiva[k] = 0
            k -= 1


    # print("Au fost gasite", len(solutii), "solutii: ", solutii)
    return solutii

    if __name__ == "__main__":
        N = 4
        solutiile = calculeaza_solutii(N)
        print(solutiile)
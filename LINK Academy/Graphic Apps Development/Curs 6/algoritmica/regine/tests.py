from django.test import TestCase

# Create your tests here.

# Numarul de regine pe tabla
N = 7
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


print("Au fost gasite", len(solutii), "solutii: ", solutii)




# k = 1
# stiva = [1]
# k = 2
# # stiva = [1, 2]
# k = 3
# stiva = [1, 3]
# k = 1
# stiva = [1, 3]   k <= N 

# stiva = [1, 4] 










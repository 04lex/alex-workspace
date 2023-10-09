from django.shortcuts import render

# Create your views here.

def este_mutare_valida(k, stiva):
        for i in range(k):
            if (stiva[i] == stiva[k]) or abs(stiva[k]-stiva[i]) == abs(k - i):
                return False
        return True

def backtracking(N):

    # Reginele puse pe tabla
    stiva = [0] * N
    print(stiva)
    # Nivelul de regine (cat sunt pe tabla)
    k = 0
    solutii = []
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

    return solutii


def solutii_view(request, regine):
    nr_regine = regine

    solutii = backtracking(nr_regine)

    prima_solutie = solutii[0]

    context = { 'N' : nr_regine,
    'range_N' : range(nr_regine),
    'solutie': prima_solutie }
    return render(request, 'tabla.html', context)


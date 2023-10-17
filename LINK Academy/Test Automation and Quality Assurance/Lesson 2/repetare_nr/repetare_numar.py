# Verificarea numarului care se repeta de cele mai multe ori dintr-o lista


def cel_mai_des_numar(lista):
    intanliri = {}
    for i in lista:
        intanliri[i] = intanliri.get(i, 0) + 1

    de_cele_mai_multe_ori = 0
    cele_mai_dese = []

    for v in intanliri:
        if intanliri[v] > de_cele_mai_multe_ori:
            de_cele_mai_multe_ori = intanliri[v]
            cele_mai_dese = [v]
        elif intanliri[v] == de_cele_mai_multe_ori:
            cele_mai_dese.append(v)

    if len(cele_mai_dese) == 1:
        return cele_mai_dese[0]

    return cele_mai_dese
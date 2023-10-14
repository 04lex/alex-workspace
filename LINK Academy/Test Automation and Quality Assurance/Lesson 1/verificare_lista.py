# Verificarea existentei unui element intr-o lista

def este_in_lista(lista, x):
    return x in lista

def testeaza_element_in_lista():
    assert este_in_lista([1, 2, 3, 4], 3), "3 nu se afla in lista."


if __name__ == "__main__":
    testeaza_element_in_lista()
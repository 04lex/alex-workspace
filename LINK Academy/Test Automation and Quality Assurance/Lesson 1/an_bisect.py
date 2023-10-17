# Verificarea unui an bisect


# return an % 4 == 0
### DEZVOLTARE
def an_bisect(an):
    """
        daca (anul este divizibil cu 4 si anul nu este divizibil cu 100) atunci (an bisect)
        daca (anul este divizibil cu 400) atunci (an bisect)
        altfel (an obisnuit)

        Args:
            an([int]): [description]

        Returns:
        [bool]: [description]
    """

    ### V2 - one line
    return ((an % 400 == 0) or (an % 100) and (an % 4 == 0))

    ### V1 - cod normal

    # if an % 400 == 0:
    #     return True
    # elif an % 100 == 0:
    #     return False
    # elif an % 4 == 0:
    #     return True
    # else:
    #     return False
    
### TESTARE 
def testeaza_an_bisect():
    assert an_bisect(2004), "Anul ar trebui sa fie biesct"
    assert not an_bisect(2009), "Anul NU ar trebui sa fie biesct"
    assert an_bisect(2000), "Anul ar trebui sa fie biesct"
    assert not an_bisect(2100), "Anul NU ar trebui sa fie biesct"
    assert not an_bisect(1800), "Anul NU ar trebui sa fie biesct"


if __name__ == "__main__":
    testeaza_an_bisect()
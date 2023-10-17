

def este_palindrom(cuvant):
    ### V2 (mai complex)
    # return cuvant == "".join(reversed(cuvant))

    ### V1
    # in cazul unui fals pozitiv (a, "blank", etc) si are mai putin de 3 caractere, codul returneaza false.
    if len(cuvant) < 3:
        return False
    # transformam orice cuvant (capitalizat) in lowercase
    cuvant = cuvant.lower()
    return cuvant == cuvant[::-1]

    
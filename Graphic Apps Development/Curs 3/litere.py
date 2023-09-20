value = "te iubesc"
VOCALE = ["a", "e", "i", "u", "u"]

# Da-mi litera daca litera nu se afla in vocale, daca se afla in vocale, vocala + p + vocala.
lista_de_litere = [ litera if litera not in VOCALE else litera + "p" + litera for litera in value ]
print(lista_de_litere)

value = "".join(lista_de_litere)
print(value)
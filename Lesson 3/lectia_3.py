# VARIANTA 1

# x = 3
# y = 4

# z = x
# x = y
# y = z

# VARIANTA 2

# print(x)
# print(y)

# x = 3
# y = 4

# x, y = y, x

# print(x)
# print(y)



# x = 15
# y = x + 30
# print(x)
# print(y)


# x = "123" + "abc"
# print(x)
# du-te la X ca sa gasesti valoarea respectiva pentru output

# print("123" + "abc")
# printeaza valoarea, dar nu este acordata nimanui

# x = 3 * "abc_"
# print(x)
# inmultesc 3 string-uri

# x = "3" * "abc_"
# print(x)
# nu stiu sa inmultesc 2 string-uri








# x = 3.7 * "abc"
# print(x)
# cum il impart pe fiecare cu zecimala, 0.7 x a?




# x = int(62.8)
# print(x)
# alege doar numarul intreg


# m = 75 / 10
# print(m)




# n = not True
# print(n)

# x = 1900
# y = 20

# print(x+y)


# Creati un program care ia doua numere de la utilizator, le aduna si afiseaza rezultatul

# V1 - Hardcodez, in cazul in care nu stiu si ii dau numerele
# x = 19
# y = 11
# z = x + y
# print(z)




# V2 - Iau de la tastatura input
# x = input("Introduceti pe X: ")
# x = float(x)

# print(type(x))

# y = input("Introduceti pe Y: ")
# y = float(y)

# print(y)

# print(x + y)



# V1
# x = int(input("Introduceti pe X: "))

# V2
# x = input("Introduceti pe x: ")
# x = int(x)



# print(type(x))
# print(x)x


# Introduc suma in LEI pentru exchange in USD, EUR.

# suma_in_lei = input("Introduceti suma in RON: ")
# suma_in_lei = float(suma_in_lei)

# euro_lei = 4.9
# usd_lei = 5.1

# suma_in_euro = suma_in_lei / euro_lei
# suma_in_usd = suma_in_lei / usd_lei

# print("Aveti ", str(suma_in_euro), "Euro")
# print("Aveti ", str(suma_in_usd), "Dolari")

# Incercarea mea pt 20% TVA

# x = input("Introduceti suma fara TVA: ")
# x = float(x)

# y = x + x / 20

# print("20 la suta din ", x, "LEI cu TVA este", y)



# euro_lei = 4.9
# usd_lei = 5.1

# Silviu vvvvvvvvvvv
# suma_fara_TVA = float(input("Introduceti suma fara TVA: "))
# TVA = 20
# suma_in_euro = suma_in_lei / euro_lei
# suma_in_usd = suma_in_lei / usd_lei

# # suma_cu_TVA = suma_fara_TVA + 20/100 * suma_fara_TVA
# # print(suma_cu_TVA)



# Incercarea mea pt 20% tva
# x = input("Introduceti suma fara TVA: ")
# x = float(x)

# y = x + x / 20

# print("20 la suta din ",x , "LEI cu TVA este", y)

# Dupa modelul exercitiului anterior, calculati pretul cu TVA al apartamentelor:
# Daca pretul < 140K, TVA 5%
# Daca pretul > 140K, TVA 20%

suma_fara_TVA = float(input("Introduceti pretul apartamentului: "))
TVA5 = 5
TVA20 = 20

suma_cu_TVA5 = suma_fara_TVA + 5/100 * suma_fara_TVA
suma_cu_TVA20 = suma_fara_TVA + 20/100 * suma_fara_TVA

if suma_fara_TVA <= 140000:
    print(suma_cu_TVA5)
elif suma_fara_TVA > 140000:
    print(suma_cu_TVA20)

# Silviu
suma_fara_TVA = float(input("Introduceti suma fara TVA: "))
TVA = 20

suma_cu_TVA = suma_fara_TVA + 20/100 * suma_fara_TVA
print(suma_cu_TVA)
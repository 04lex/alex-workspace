


# if 1:
#     print("always")
# else:
#     print("never")



# a = 1, # Acelasi lucru cu a = (1), este tuple
# print(type(a))


# # TUPLE
# a_tuple = (1, 2, 3, 4, 5)

# # LIST
# a_lista = [1, 2, 3, 4, 5]

# # DICT
# a_dictionar = {"a":1, "b":2, "c":3, "d":4, "e":5}

# # SET
# a_set = {1.2, 2, 3, 4, 5, 1, 2, 3, 4 ,5 ,1 ,1, 2, 2, 3, 4, 5}

# In program sunt definite variabilele startDate si endDate care reprezinta anul initial si cel final.
# Trebuie creat un program care, pe baza acestor doua valori, va afisa lista anilor.
# Aplicatia trebuie sa aiba o iesire identica celei de mai jos:
# Allowed years: 2010 - 2015.

# # EU
# startDate = 2010
# endDate = 2015

# for i in range(2010, 2015):
#     print(f"Allowed years: {i}")


# Silviu V1

# startDate = int(input("Introduceti primul an: \n"))
# endDate = int(input("Introduceti al doilea an: \n"))

# r = range(startDate, endDate + 1)

# for i in r:
#     print(i)


# y = startDate
# while y <= endDate:
#     print(y)
#     y += 1

# print(f"Anii de la {startDate} pana la {endDate}")



# x = "hello"
# y = "hello"

# while True:
#     nume = input("Care este numele tau? \n")
#     if not nume:
#         print("Te rog introdu un nume")
#         continue
#     else:
#         print(f"Bine ai venit la curs {nume}")
#     print("Mult succes in noul an universitar")





# suma = 0

# while True:
#     x = input("Introduceti numarul \n")
#     if x.isnumeric():
#         x = int(x)
#         suma = suma + x
#         print("X este numeric")
#         print(f"Suma este {suma}")
#     elif not x:
#         print(f"Suma este {suma}")
#         suma = 0
#     else:
#         print("X este nemernic ! ! !")



# x = 10
# y = 10
# suma = x + y

# z = 30
# suma += z
# print(suma)






# Un calculator care citeste ID-ul la intrarea intr-un club unde baietii trebuie sa fie 18+, fetele 16+ dar nimeni mai in varsta de 70.

#TEST

# varsta = int(input("Introduceti varsta: \n"))
# genul = str(input("Introduceti genul: \n"))

# male = 18
# male = int(male)

# female = 16
# female = int(female)

# if varsta >= male:
#     print("Access (M)")



# Silviu

# varsta = int(input("Introduceti varsta: \n"))
# if not varsta in range(16, 70): # echivalent cu -> if varsta in range(0, 16) or varsta in range(70, 1000):

# while True:
#     if not varsta in range(16, 70):
#         print("Ghinion")
#     elif varsta >= 18:
#         print("Acces la toata lumea.")
#     else:
#         gen = input("Introduceti genul: ")
#         if gen in ["masculin", "barbat"]:
#             print("Ghinion")
#         elif gen in ["feminin", "femeie"]:
#             print("Acces")
#         else:
#             print("Acces")

# VARIANTA MAI SCURTA: 
# while True:
#     if not varsta in range(16, 70):
#         print("Ghinion")
#     elif varsta >= 18:
#         print("Acces la toata lumea.")
#     elif input("Introduceti genul\n") in ["feminin", "femeie"]:
#             print("Access")
#     else:
#         print("Ghinion")



# V2

varsta_maxima = 70
varsta_minima_dict = {"m":18, "f":16}

while True:
    gen = input("Introduceti genul\n")
    varsta_minima = varsta_minima_dict[gen]

    varsta = int(input("Introduceti varsta\n"))

    if varsta in range(varsta_minima, varsta_maxima):
        print("Access")
    else:
        print("Ghinion")
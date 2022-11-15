# Creati un program in care utilizatorul va insera o suma intraga
# Programul trebuie sa calculeze si sa afiseze numarul corespunzator de bancnote, unde in program sunt definite bancnotele cu valorile: 10, 5, 2 si 1.

# V1 - Programul meu

# Suma
# s = int(input("Introduceti salariul: "))

# # Bancnote
# b10 = s // 10
# b5 = (s % 10) // 5
# b2 = (s % 5) // 2
# b1 = b2 % 2

# print("Aveti suma: ", s)
# print("Bancote de 10: ", b10)
# print("Bancote de 5: ", b5)
# print("Bancote de 2: ", b2)
# print("Bancote de 1: ", b1)





# V2 - Silviu

# suma = int(input("Introduceti suma: \n"))

# nr_bancnote_10 = suma // 10
# print("Numarul de bancnote de 10 este: ", nr_bancnote_10)

# # Calculez ce rest ramane dupa ce imparte la 10
# rest_bancnote_10 = suma % 10

# nr_bancnote_5 = rest_bancnote_10 // 5
# print("Numarul de bancnote de 5 este: ", nr_bancnote_5)

# rest_bancnote_5 = rest_bancnote_10 % 5
# nr_bancnote_2 = rest_bancnote_5 // 2
# print("Numarul de bancnote de 2 este: ", nr_bancnote_2)

# nr_bancnote_1 = rest_bancnote_5 % 2
# print("Numarul de bancnote de 1 este: ", nr_bancnote_1)



# V3 - Silviu

# suma = int(input("Introduceti suma: \n"))

# nr_bancnote_10 = suma // 10

# print("Numarul de bancnote de 10 este: ", nr_bancnote_10)

# nr_bancnote_5 = (suma % 10) // 5
# print("Numarul de bancnote de 5 este: ", nr_bancnote_5)

# nr_bancnote_2 = (suma % 10) % 5 // 2
# print("Numarul de bancnote de 2 este: ", nr_bancnote_2)

# nr_bancnote_1 = (suma % 10) % 5 % 2
# print("Numarul de bancnote de 1 este: ", nr_bancnote_1)


# V4 - Silviu

# suma = int(input("Introduceti suma: \n"))
# print("Numarul de bancnote de 10 este: ", suma // 10)
# print("Numarul de bancnote de 10 este: ", (suma % 10) // 5)
# print("Numarul de bancnote de 10 este: ", (suma % 10) % 5 // 2)
# print("Numarul de bancnote de 10 este: ", (suma % 10) % 5 % 2)




# FUNCTIE
# def printeaza_un_mesaj():
#     print("Acest mesaj este printat de catre functie")

# ITERATIE
# for i in range(5):
#     printeaza_un_mesaj()

# def adunare(a, b):
#     print("Rezultatul adunarii este:", a + b)

# adunare(2, 3)





# V5 

# suma = int(input("Introduceti suma: \n"))
# def printeaza_mesajul_cu_bancnote (x, y):
#     print("Numarul de bancnote de", x, "este:", y)


# printeaza_mesajul_cu_bancnote (10, suma // 10)
# printeaza_mesajul_cu_bancnote (5, (suma % 10) // 5)
# printeaza_mesajul_cu_bancnote (2, (suma % 10) % 5 // 2)
# printeaza_mesajul_cu_bancnote (1, (suma % 10) % 5 % 2)



# In cadrul programului este definita o suprafata in cadranul XoY: x,y,width si height.
# Utilizatorul introduce coordonatele userx si usery in program, iar programul afiseaza True 
# daca punctul se gaseste in cadranul suprafetei definite sau False daca se gaseste in afara acesteia

# x0 = 10
# # x0 = int(input("Introduceti x0"))
# y0 = 10
# width = 50
# height = 60

# x1 = x0 + width
# y1 = y0 + height

# x2 = 50
# y2 = 160

# VARIANTA 1
# if (x0 < x2 and x2 < x1) and (y0 < y2 and y2 < y1):
#     print("Punctul se afla in cadran")
# else:
#     print("Punctul nu se afla in cadran")


# VARIANTA 2
# rezultat = (x0 < x2 and x2 < x1) and (y0 < y2 and y2 < y1)
# print("Punctul se alfa in cadran:", rezultat)


# VARIANTA 3
# if x0 < x2 and x2 < x1 and y0 < y2 and y2 < y1:
#     print("Punctul se afla in cadran")
# else:
#     print("Punctul nu se afla in cadran")

# VARIANTA 4 - operator ternar
# print("Punctul se afla in cadran") if x0 < x2 and x2 < x1 and y0 < y2 and y2 < y1 else print("Punctul nu se afla in cadran")

# if 3 > 2:
#     print("YES")
# else:
#     print("NO")

# print("YES") if 3 < 2 else print("NO")


# VARIANTA 5 - if imbricat
# if x0 < x2 < x1: 
#     if y0 < y2 < y1:
#         print("Se afla in cadran")
#     else:
#         print("Nu se afla in cadran")
# else:
#     print("Nu se afla in cadran")


# VARIANTA 6
# if x0 < x2:
#     if x2 < x1:
#         if y0 < y2:
#             if y2 < y1:
#                 print("Se afla in cadran")
#             else: 
#                 print("Nu se afla in cadran, y2 > y1")
#         else: 
#                 print("Nu se afla in cadran, y0 > y2")
#     else: 
#                 print("Nu se afla in cadran, x2 > x1")
# else: 
#                 print("Nu se afla in cadran, x0 > x2")


# a = [1, 2, 3, 4, "Hello"]
# print(2 in a)

# b = ["H", "e", "l", "l", "o"]
# if "h" in b:
#     print("L-am gasit pe h")
# else:
#     print("Nu l-am gasit pe h, nu exista, nu stiu")




# x = [1, 2, 3]

# y = [1, 2, 3]

# m = 1
# n = 1

# print("x == y", x == y)
# print("m == n" ,m == n)

# print("x is y" ,x is y)
# print("m is n" ,m is n)


# Exercitiul cu parola
# In cadrul programului sunt definite variabilele: db_username, db_password.
# Utilizatorul introduce numele de utilizator si parola.
# La iesire se afiseaza True daca numele de utilizator si parola corespund celor din program sau False daca acestea nu corespund.

# db_username = ["peter", "kelly", "poppy"]
# db_password = ["123", "321", "868"]

# username = input("Introduceti username-ul: \n")
# password = input("Introduceti parola: \n")


# if username in db_username and password in db_password:
#     print("Access granted")
# else: 
#     print("Password/Username incorrect")


# VARIANTA 1

db_username = "peter"
db_password = "123"

input_username = input("Introduceti username-ul: \n")
input_password = input("Introduceti parola: \n")

# if db_password == input_password and db_username == input_username:
#     print("ACCESS GRANTED")
# else:
#     print("DENIED")

# VARIANTA 2
# print("ACCESS GRANTED") if db_password == input_password and db_username == input_username else print("DENIED")

# VARIANTA 3
if db_password == input_password:
    if db_username == input_username:
        print("Access Granted")
    else:
        print("Denied - Wrong user")
else:
    print("Deneid - Wrong password")

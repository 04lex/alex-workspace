

# if 2 > 1:
#     print("Conditia este adevarata")


# # SE PRINTEAZA 
# conditie = bool(-1)
# conditie = bool("0")
# conditie = bool(-0.1)

# # NU SE PRINTEAZA
# conditie = bool(0)
# conditie = bool("")
# conditie = bool(0.0)
# conditie = bool([])



# if conditie:
#     print("Conditia este adevarata")
# else:
#     print("Neadevarat")

# # Acelasi cod prin operator ternar:
# print("Conditia este adevarata") if conditie else print("Neadevarat")



# Exercitiul cu ghicitul
# In program, utilizatorul introduce un numar de la 1 la 10, iar calculatorul isi imagineaza
# un numar de la 1 la 10. Programul afiseaza mesajul daca utilizatorul a ghicit numarul 
# imaginat de calculator.

# VARIANTA MEA - Hardcodat
# calculator = 7

# numar_introdus = input(int("Introduceti un numar de la 1 la 10: \n"))
# print("Ai ales numarul", numar_introdus)

# if numar_introdus == calculator:
#     print("Ai ghicit, numarul este 7")
# else:
#     print("Nu ai ghicit, mai incearca")




# Silviu V1 - Calculatorul introduce un numar hardcodat
# calculator = 4
# ghicit = input("Introduceti un numar")
# ghicit = int(ghicit)

# print("Ai ghicit") if calculator == ghicit else print("Nu ai ghicit")
    

# Silviu V2 - Generam un numar
# import random
# calculator = random.randint(1, 10)

# ghicit = input("Introduceti un numar")
# ghicit = int(ghicit)

# print("Ai ghicit") if calculator == ghicit else print("Nu ai ghicit,", calculator)

# x = 3
# print("Numarul este", x, ".", sep="")
# print(f"Numarul este {x}.") Compilatorul formateaza string-ul




# V3 Silviu - Rezultatul este pus intr-o variabila
# import random
# calculator = random.randint(1, 10)

# ghicit = input("Introduceti un numar: ")
# ghicit = int(ghicit)

# rezultat = (calculator == ghicit)

# if rezultat:
#     print("Ai ghicit!")
# else:
#     print("Nu ai ghicit!")

#     print(calculator)




# V4 Silviu

# def compara(mere, pere):
#     if mere == pere:
#         print("Ai ghicit")
#     else:
#         print("Nu ai ghicit")



# import random
# calculator = random.randint(1, 10)

# ghicit = input("Introduceti un numar: ")
# ghicit = int(ghicit)


# compara(calculator, ghicit)
# print(calculator)





# Programul cere de la utilizator sa introduca limba dorita.
# Dupa introducerea limbii, programul afiseaza mesajul in limba aleasa

limba_user = input(str("Enter language: \n"))
en = "en"
ro = "ro"

def language(limba, en):
    if limba_user == en:
        print("Hello")
    else:
        print("Please choose a language")



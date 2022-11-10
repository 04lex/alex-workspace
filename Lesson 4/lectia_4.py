



# V1 - Scrise de fiecare data, e nevoie sa fie modificate in fiecare linie

# val_fara_TVA = float(input("Introduceti pretul fara TVA: "))

# if val_fara_TVA < 140:
#     TVA = 0.05
#     vaL_cu_TVA = val_fara_TVA + TVA * val_fara_TVA
#     print("Valoarea cu TVA: ", vaL_cu_TVA)
# else:
#     TVA = 0.19
#     vaL_cu_TVA = val_fara_TVA + TVA * val_fara_TVA
#     print("Valoarea cu TVA: ", vaL_cu_TVA)





# V2 - Scrise o singura data DRY (Do Not Repeat Yourself)

# val_fara_TVA = float(input("Introduceti pretul fara TVA: "))

# if val_fara_TVA < 140:
#     TVA = 0.05
# else:
#     TVA = 0.19

# vaL_cu_TVA = val_fara_TVA + TVA * val_fara_TVA

# print("Valoarea cu TVA: ", vaL_cu_TVA)





# Exemplu mai putin eficient, dar acelasi rezultat

# val_fara_TVA = float(input("Introduceti pretul fara TVA: "))
# val_cu_TVA_5 = val_fara_TVA + 0.05 * val_fara_TVA
# val_cu_TVA_19 = val_fara_TVA + 0.19 * val_fara_TVA

# if val_fara_TVA < 140:
#     print("Valoarea cu TVA: ", val_cu_TVA_5)
# else:
#     print("Valoarea cu TVA: ", val_cu_TVA_19)




# Utilizatorul introduce TVA-ul

# val_fara_TVA = float(input("Introduceti pretul fara TVA: "))
# TVA = float(input("Introduceti TVA-ul: "))
# vaL_cu_TVA = val_fara_TVA + TVA * val_fara_TVA
# print("Valoarea cu TVA: ", vaL_cu_TVA)







# Creati un program care va cere de la utilizator valoarea razei si va afisa aria cercului.
# V1 - versiunea mea

# R = float(input("Introduceti raza: "))
# pi = 3.14

# aria = pi * R**2

# print("Aria este:",aria)


# V2 - Silviu

# pi = 3.14
# raza = float(input("Introduceti raza cercului: "))

# aria = pi * raza * raza
# print("Aria cercului este", aria)









# Creati un program care va prelua de la utilizator un numar si va verifica daca este par sau impar
# Enter number? 3 ; Number is even: False

# V1 - varianta mea

numar = int(input("Introduceti numarul: "))
x = numar % 2
# % va lua restul din impartirea numarului la 2, rest 0 = s-a impartit si nu are rest => par. 
# rest = 1... + inseamna ca nu se imparte fix si este impar

if x == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")





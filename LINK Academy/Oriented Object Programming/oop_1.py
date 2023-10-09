# x = 1
# print(type(x))
# print(isinstance(x,bool))
# print(isinstance(x,int))

# l = [ 42, 13 , 61 , 2 , -42 , 868 , 1, -11, -32, 300, 38384]
# print(max(l))

# l.sort(reverse=True) # reverse este parametru implicit

# print(l)

# print(l[-1])
# print(l[0])



# def calcul_pret_cu_tva(pret, TVA=19): # parametru implicit TVA=19, se adauga singur in functie unde nu are asignat altul
#     return pret + pret * TVA / 100

# print(calcul_pret_cu_tva(100, 20))
# print(calcul_pret_cu_tva(100))
# print(calcul_pret_cu_tva(100))
# print(calcul_pret_cu_tva(TVA=19, pret=100))

# print(list(range(10))) # 1 parametru implicit obligatoriu, ceilalti 2 se adauga
# print(list(range(3, 10)))
# print(list(range(5, 10, 2)))



# x = range # x-ul are aceleasi proprietati cu range
# print(list(x(3,10)))

# def check_if_x_exist(x, lst): # aceeasi chestie dar lunga
#     if x in lst:
#         return True
#     else:
#         return False




# def adunare(x, y = 2, z = 3):
#     return x + y + z


# print(adunare(1,2,3))
# print(adunare(1,2))
# print(adunare(1))




# def check_if_x_exist(x, lst): # varianta frumoasa si simpla
#     return x in lst


# print(check_if_x_exist(1, [3, 41, 52, 53, 1, 32, 1]))
# print(check_if_x_exist(11, [3, 41, 52, 53, 1, 32, 1]))
# print(check_if_x_exist(lst = [3, 41, 52, 53, 1, 32, 1], x = 11))


# Hardcodat pentru "caiac", le va verifica doar pe primele 3
# def are_palindrom(s):
#     if s[0] == s[-1] and s[1] == s [-2] and s[2] == s[-3]:
#         return True
#     else:
#         return False




# def are_palindrom(s):
#     for i in range(len(s)//2):
#         if s[i] != s[-i-1]:
#             return False
#     return True


# def are_palindrom_v2(s):
#     # s[::-1] inversul lui s
#     return s == s[::-1]


# def are_anagram(s1, s2):
#     pass


# print(are_palindrom_v2("caiac"))
# print(are_palindrom_v2("hello"))


# Desenez o cutie hardcodata
# def render(x, y):
#     print("##########")
#     print("#        #")
#     print("#        #")
#     print("#        #")
#     print("##########")



# def render(x, y):
#     print("#"*x)
#     for _ in range(y-2):
#         print("#"+ " " * (x-2)  + "#")
#     print("#"*x)

# render(9,5)



# Varianta in care se adauga manual cate un numar
# def adunare(x, y, z):
#     return x + y + z

# Varianta cu * in care adaugam in returnare oricate
# def adunare(*x):
#     suma = 0
#     for i in x:
#         suma += i
#     return suma


# print(adunare(1, 3, 3, 10, 15))


# * este echivalentul unui tuplu in def
# ** este echivalentul unui dictionar in def


# def produs(**a):
#     print(a)
#     print(type(a))
#     p = 1
#     for i in a:
#         p *= a[i]
#     return p

# print(produs(x=1, y=2, z=3, w=10, t=10))


# print(1, 2, 3, 4, sep="**") # separatorul poate fi denumit



# # VARIANTA 1
# def aria(raza):
#     return raza ** 2 * 3.14


# # VARIANTA 2
# def aria(raza, puterea, pi):
#     return raza ** puterea * pi
# print(aria(1, 2, 3.14))


# # VARIANTA 3
# def aria(*args):
#     raza = args[0]
#     puterea = args[1]
#     pi = args[2]
#     return raza ** puterea * pi

# print(aria(1, 2, 3.14))


# # VARIANTA 4 = keyword args
# def aria(**kargs):
#     raza = kargs["raza"]
#     puterea = kargs["puterea"]
#     pi = kargs["pi"]
#     return raza ** puterea * pi

# print(aria(raza=1, puterea=2, pi=3.14))

# ceva = 10
# print(ceva)

# def mai_mare_decat_ceva(x):
#     global ceva
#     ceva = 15
#     return x > ceva

# print(mai_mare_decat_ceva(14))
# print(ceva)




# x = 0

# def incrementeaza():
#     # global x
#     x = 0
#     x += 1
#     y = 0
#     return x, y

# print(incrementeaza())
# print(x)
# print(incrementeaza())
# print(x)
# print(incrementeaza())
# print(x)





# class Pisica:
#     def __init__(self, x, culoare="rosu"):
#         print("Este apelata def __init__(self)")
#         self.varsta = x
#         self.culoare = culoare

#     def miauna(self):
#         print("miau " * self.varsta)

#     def toarce(self):
#         print("brrr" * 10)


# rino = Pisica(4, "gri")
# # print(rino)
# # print(type(rino))
# rino.miauna()
# rino.toarce()
# print(rino.culoare)

# tommy = Pisica(3, "galben")
# tommy.miauna()
# tommy.toarce()
# print(tommy.culoare)


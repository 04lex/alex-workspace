# def esteMaiMare(a, b):
#     return a > b

# print(esteMaiMare(1, 3))



# O lista care printeaza toti anii bisecti dintre primul si al doilea an.
# primulAn = 2001 
# alDoileaAn = 2022


# Varianta 1
# def calculeazaAniiBisecti(start, stop):
#     rezultat = []
#     for i in range(start, stop):
#         if not i % 4:
#             rezultat.append(i)
#     return rezultat

# anii = calculeazaAniiBisecti(primulAn, alDoileaAn)
# print(anii)

# print("-------")

# # Varianta 2
# primulAn = primulAn if not primulAn % 4 else (primulAn // 4) * 4 + 4
# primulAn = (primulAn // 4) * 4 + 4 if primulAn % 4 else primulAn

# for i in range(primulAn, alDoileaAn, 4):
#     print(i)


# if primulAn % 4:
#     primulAn = (primulAn // 4) * 4 + 4
# else:
#     primulAn = primulAn

# # Varianta 3

# def calculeazaAniiBisecti(start, stop):
#     return [ i for i in range(start, stop) if not i % 4]




# Varianta 4 

# def calculeazaAniiBisecti(start, stop):
#     start = (start // 4) * 4 + 4 if start % 4 else start
#     return [ i for i in range(start, stop, 4) ]



# Varianta 5 

# def calculeazaAniiBisecti(start, stop):
#     start = (start + 4) // 4 * 4  if start % 4 else start
#     return [ i for i in range(start, stop, 4) ]


# anii = calculeazaAniiBisecti(primulAn, alDoileaAn)
# print(anii)



# Ce va printa in consola?


# fruits = ["fox", "bear", "rabbit"]
# print(fruits[-1])



# x = range(4)
# for n in x:
#     print(n)

# aTuple = (200, 300, 400, 500, 600, 800)
# print(aTuple[:-1])

# i=0
# a=0
# while i<10:
#     a+=i
#     i+=2

# print(i)


# a=15
# if a<10:
#     print("test")


# var_a = True
# var_b = False
# if var_a==True:
#     if var_b==False:
#         print("1")
#     else: print("2")
# else: print("3")


# cities = ["Berlin", "Paris", "Moscow"]
# for e in range(len(cities)):
#     cities[e]=cities[e]+"2"

# print (cities)



# countries = {'UK':'London', 'DE':'Berlin', "FR":'Paris'}
# list1 = []
# for c in countries:
#     list1.append(c)
# print(list1)


# England = {"capital": "London", "population": 8768000}
# print(England.get("capital"))


# s = "aaaa1"
# print(min(s))


# list1 = [1,2,3]
# list2 = [4,5,6]
# print(max(list1))
# print(max(list2))


# city1 = "LONDON";
# city2 = "MOSCOW"
# print(city1[-4:]+city2[-2:])


# capital = "London"
# if len(capital) == 5:   
#     print(False)
# else:   
#     print(True) 


# cities = ('Belgrade', 'Paris', 'Berlin', 'London')
# print(len(cities))

# d = {'key0':'value0', 'key1':'value1'}
# print(d['key0'])


# England = {"capital": "London", "population": 8768000}
# print(list(England.keys()))

# lista = {'key2':'val2', 'key1':'val1'}.sort()

# print(lista)



# m_list = [['e1', 'e2'], ['London', 'Paris'], ['Susan', 'Maria']]
# print[0][3]



# cities = [['New York', 'London'], ['Paris', 'Berlin']]
# cities[0].pop(1)
# print(cities)


# lst = ["a", "b", "c"]
# lst_iterator = iter(lst)
# print(next(lst_iterator), next(lst_iterator))



# x = lambda b,a : 10*b+a
# print(x(2,4))


# def x2(a):   
#    for x in range(a):
#        yield x*x

# print(list(x2(4)))

# def first():
#     print("1")
# def first():
#     print("2")
# first()



# def x2(a):
#     return a*a
# x = [1,2,3,4,5]
# print(list(map(x2, x))) 


import math as mat
print(mat.pi)

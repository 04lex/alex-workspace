# x = 10
# def suma(*x):
#     x = sum(x)
# def calcul_tva():
#     global x
#     x += suma(1,3,5)
# print(x)
# calcul_tva()



# x = 500
# def glob():
#     global x
#     x = 100
# glob()
# print(x)



# definesc clasa
# x = 10
# class Student:
#     def __init__(self, age, name):
#         print("A fost creat un obiect")
#         self.age = age
#         self.name = name
        

#     def __str__(self):
#         return f"Studentul {self.name} are varsta {self.age}"
# # Definesc o noua metoda in care adaug un nume 
#     def adaugaNume(self, newName):
#         if newName.isalpha ():
#             self.name = self.name + " " + newName
#         else:
#             print("Numele introdus nu este valid")

#     def esteAdult(self):
#         return self.age > 18

# # creez un obiect

# std1 = Student(26, "Georgescu") # __init__
# print(std1) # __str__

# # std1 -> il transforma in string 
# print(std1.name)

# print(std1.esteAdult())

# nouNume = input(f"Introduceti noul nume al studentului {std1.name}:\n")

# std1.name = std1.name + " " + nouNume
# print(std1)

# std2 = Student(30, "Ionescu")
# print(std2)

# nouNume = input(f"Introduceti noul nume al studentului {std2.name}:\n")
# std2.adaugaNume(nouNume)
# print(std2)






# class Calculator:
#     def __init__(self, operand1, operand2):
#         self.operand1 = operand1
#         self.operand2 = operand2

#     def __str__(self):
#         return f"Operand1= {self.operand1} \nOperand2= {self.operand2}"

#     def add(self):
#         return self.operand1 + self.operand2

#     def sub(self):
#         return self.operand1 - self.operand2
        
#     def mul(self):
#         return self.operand1 * self.operand2


# calc = Calculator(10, 30)
# print(calc)

# print(f"Adunarea operanzilor este {calc.add()}\nScaderea operanzilor este {calc.sub()}\nInmultirea operanzilor este {calc.mul()}")



# Versiunea mea, neterminata

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"Coordonata x = {self.x} \nCoordonata y = {self.y}")

#     def move(self, newCoordx, newCoordy):
#         if newCoordx.isnumeric() and newCoordy.isnumeric():
#             self.x = newCoordx
#             self.y = newCoordy
#         else:
#             print("Ati introdus numere invalide")


#     def setToOrigin(self):
#         pass

#     def dist(self):
#         pass

# coord = Point(10, 20)
# coord.show()

# newCoordx = (input(f"Introduceti noile coordonate pentru x:"))
# newCoordy = (input(f"Introduceti noile coordonate pentru y:"))
# print(coord.show())



# Silviu
# import math

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x},{self.y})"

#     def show(self):
#         return "Punctul se afla la " + str(self)

#     def move(self, newX, newY):
#         self.x = newX
#         self.y = newY

#     def setToOrigin(self):
#         # self.x, self.y = 0, 0
#         self.move(0, 0)

#     def dist(self, otherPoint):
#         cateta1_la_patrat = (self.x - otherPoint.x) ** 2 
#         cateta2_la_patrat = (self.y - otherPoint.y) ** 2
#         ipotenuza_la_patrat = cateta1_la_patrat + cateta2_la_patrat 
#         return math.sqrt(ipotenuza_la_patrat)


# p1 = Point(3, 4)
# p2 = Point(10, 10)
# print(p1.dist(p2))
# print(p2.dist(p1))







# AM INCERCAT....

# class Account:
#     def __init__(self, contbancar, newSum):
#         self.contbancar = contbancar
#         self.newSum = newSum

#     def __str__(self):
#         return f"{self.contbancar}"

#     def showBalance(self):
#         return "Sold curent: " + str(self)

#     def withdraw(self):
#         return self.contbancar - self.newSum

        


    
# cont = Account(100_320)
# print(cont.showBalance())
# retragere = input("Introduceti suma pe care doriti sa o scoateti din sold: ")
# cont.withdraw(10000)
# print(cont.showBalance())











class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def showBalance(self):
        return f"Contul are: {self.balance}"

    def addMoney(self, money):
        self.balance += money

    def withdrawMoney(self, money):
        if self.balance > money:
            self.balance -= money
        else:
            print("Mergi la munca")
    


account1 = Account()
account2 = Account(100)
print(account1.showBalance())
print(account2.showBalance())

account2.withdrawMoney(50)
print(account2.showBalance())

account2.withdrawMoney(50)
print(account2.showBalance())








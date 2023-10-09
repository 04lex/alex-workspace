# class A:
#     def a(self):
#         print("A")
#     def b(self):
#         self.a()


# class B(A):
#     def a(self):
#         print("B", end='')
#     def do(self):
#         self.b()

# B().do()



# class Vehicul:
#     def pornesteMotor(self, sunet="Brrr", de_x_ori = 3):
#         print(sunet*de_x_ori)


# vehicul = Vehicul()
# vehicul.pornesteMotor()
# vehicul.pornesteMotor("C^r^r^r")
# vehicul.pornesteMotor("R", 6)






# MENU = {
#     "1":"carte noua",
#     "2":"modificare carte",
#     "3":"stergere carte",
#     "4":"listarea tuturor cartilor",
#     "5":"iesire din program"
# }

# print(MENU)

# class Meniu:

#     def __init__(self, *args, **kargs):
#         print(args)
#         print(kargs)

#         self.optiuni = kargs
#         for a in range(len(args)):
#             self.optiuni[a+1] = args[a]


#     def __str__(self):
#         lista_optiuni = ""
#         for opt in self.optiuni:
#             lista_optiuni += f"Apasati {opt} pentru {self.optiuni[opt]}\n"
#         return lista_optiuni


#     def __len__(self):
#         return len(self.optiuni)


# meniuObj = Meniu(a="carte noua", b="modificare carte", c="stergere carte")
# print(meniuObj)

# print(len(meniuObj))



# varianta = input("Alegeti o varianta")




class Biblioteca:
    def __init__(self, *carti):
        self.carti = list(carti)

    def __str__(self):
        lista_carti = ""
        for carte in self.carti:
            if not lista_carti:
                lista_carti += carte
            else:
                lista_carti += ", " + carte
        return lista_carti

    def __len__(self):
        return len(self.carti)

    def __iadd__(self, carte):
        self.carti.append(carte)
        return self

    def __isub__(self, carte):
        if carte in self.carti:
            index = self.carti.index(carte)
            self.carti.pop(index)
        return self

# link = Biblioteca(carte1, carte2, carte3, carte4)
# print(link)
# print(len(link))

# link += "Django"
# print(link)
# print(len(link))

# link -= "OOP"
# print(link)
# print(len(link))



# class Student:
#     CURSURI = {"Fundamentals":8, "OOP":6, "Networking":6, "HTML":6}
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def getCourseList(cls):
#         return tuple(cls.CURSURI.keys())

#     @classmethod
#     def getTotalNoOfHours(cls):
#         return sum(cls.CURSURI.values())

# class Professor:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age



# print(Student.CURSURI)
# print(Student.getCourseList())
# print(Student.getTotalNoOfHours())

# Student.CURSURI['MySQL'] = 8

# print(Student.CURSURI)
# print(Student.getCourseList())
# print(Student.getTotalNoOfHours())



# obiect1 = Student("Alin", 20)
# obiect2 = Student("Andreea", 20)

# print(type(obiect1) == type(obiect2))









# def o_alta_functie():
#     print('Buna ziua')


# def decorator(func):
#     print('Decoratorul a fost chemat')
#     return func


# @decorator
# def o_functie():
#     print("Hello, sunt o_functie")


# o_functie()




def printFuncName(func):
    def innerFunc(a,b):
        print(func.__name__, 'a fost chemata')
        func(a,b)
    return innerFunc

@printFuncName
def suma(a,b):
    print(a+b)

@printFuncName
def diferenta(a,b):
    print(a-b)


suma(10,5)
diferenta(20,5)
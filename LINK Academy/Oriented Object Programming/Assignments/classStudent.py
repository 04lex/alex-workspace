class Student:
    def __init__(self, name, address, phone, course, index_number):
        self.name = name
        self.address = address
        self.phone = phone
        self.course = course
        self.index_number = index_number

    def getInfo(self):
        return f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}, Course: {self.course}, Index: {self.index_number}"
    

# Name: John Benson, address: High Park 36, Phone: (507) 833-3567, Course: Geography, Index number: 123/007).

student1 = Student("John Benson", "High Park 36", "(507) 833-3567", "Geography", "123/007")
student2 = Student("Ion Popescu", "Park Ave 32", "(506) 555-3456", "Computer Science", "244/008")
student3 = Student("Jane Doe", "Hay Park 44", "(509) 777-2233", "Psychology", "808/009")

print(student1.getInfo())
print(student2.getInfo())
print(student3.getInfo())

#Encapsulation and inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

    def get_age(self):
        return self.__age

class Student(Person):     
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Age: {self.get_age()}, Roll: {self.roll}")

s = Student("Priyu", 19, 35)
s.display()

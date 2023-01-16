# Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name)

    def printAge(self):
        print(self.age)


class Student(Person):
    pass


class Teacher(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.age = 25


st1 = Student("John", 25)
st1.printName()

st2 = Teacher("Mike", 30)
print(st2.age)

st3 = Employee("Mike", 30, 5000)
print(st3.salary)

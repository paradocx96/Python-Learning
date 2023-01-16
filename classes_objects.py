class MyClass:
    i = 12345


c1 = MyClass()
print(c1.i)


class MyClassPass:
    pass


class MyClassNew:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Name: ' + self.name + ' Age: ' + str(self.age)

    def new_func(self):
        print('Hello, ' + self.name)

    def new_func2(any_param):
        print('Yor age, ' + str(any_param.age))


c2 = MyClassNew('Naivnda', 25)
print(c2.name, c2.age)
print(c2)
c2.new_func()
c2.new_func2()
c2.age = 26
c2.new_func2()
del c2.age
del c2

# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.

x = ("apple", "banana", "cherry")
y = iter(x)
print(next(y))
print(next(y))
print(next(y))

p = "banana"
q = iter(p)
print(next(q), end=" ")
print(next(q), end=" ")
print(next(q), end=" ")
print(next(q), end=" ")
print(next(q), end=" ")
print('\n')


class MyClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_class = MyClass()
my_iter = iter(my_class)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

for x in my_iter:
    print(x, end=' ')

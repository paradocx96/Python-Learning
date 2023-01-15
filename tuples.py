x = ("apple", "banana", "cherry", "apple", "orange")
print(x)
print(len(x))
print(type(x))

print(x[4])
print(x[1:3])
print(x[1:])
print(x[:3])
print(x[-4:-2])
print(x[-4:])
print(x[:-2])

# Change
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

x = ("apple", "banana", "cherry", "apple", "orange")
y = list(x)
y.append("lemon")
x = tuple(y)
print(x)

x = ("apple", "banana", "cherry", "apple", "orange")
y = ("lemon", "mango", "kiwi",)
x += y
print(x)

x = ("apple", "banana", "cherry", "apple", "orange")
y = list(x)
y.remove("banana")
x = tuple(y)
print(x)

# x = ("apple", "banana", "cherry", "apple", "orange")
# del x
# print(x)

x = ("apple", "banana", "cherry", "apple", "orange")
(one, two, three, four, five) = x
print(three)

(one, two, *three, four, five) = x
print(three)

x = ("apple", "banana", "cherry", "apple", "orange")
for i in x:
    print(i, end=' ')

print('\n')

for i in range(len(x)):
    print(x[i], end=' ')

print('\n')

i = 0
while i < len(x):
    print(x[i], end=' ')
    i += 1

print('\n')

# Joining
x = ("apple", "banana", "cherry", "apple", "orange")
y = ("lemon", "mango", "kiwi")
z = x + y
print(z)

y = x * 2
print(y)

print(x.count("apple"))
print(x.index("apple"))

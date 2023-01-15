x = ["apple", "banana", "cherry", "apple", "cherry"]
print(x)
print(type(x))
print(len(x))

print(x[1])
print(x[1:3])
print(x[:3])
print(x[1:])
print(x[-4:-2])
print(x[-4:])
print(x[:-2])

for i in x:
    print(i, end=' ')

print('\n')

x = [0, 1, 2, 3, 4, 5]

# Change
x[3] = 'newFruit'
print(x)

x[3:4] = ['newFruit1', 'newFruit2']
print(x)

# Adding
x.insert(3, 'newFruit4')
print(x)

x.append('newFruit5')
print(x)

x.extend(['newFruit6', 'newFruit7'])
print(x)

x.extend(('newFruit8', 'newFruit9'))
print(x)

# Removing
x.remove('newFruit9')
print(x)

x.pop(11)
print(x)

x.pop()
print(x)

del x[8]
print(x)

x.clear()
print(x)

x = [0, 1, 2, 3, 4, 5]
del x

# Looping
x = [0, 1, 2, 3, 4, 5]
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

[print(i, end=' ') for i in x]

print('\n')

# Sorting
x = [5, 6, 2, 4, 8, 3, 1, 9, 7, 0]
x.sort()
print(x)

x.sort(reverse=True)
print(x)

x.sort()


def sort_func(n):
    return abs(n - 5)


x.sort(key=sort_func)
print(x)

x.reverse()
print(x)

x = ["one", "two", "three", "four", "five"]
x.sort(key=str.lower)
print(x)

# Copying
x = [0, 1, 2, 3, 4, 5]
y = x.copy()
print(y)

# Joining
x = [0, 1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z = x + y
print(z)

for i in y:
    x.append(i)
print(x)

x.extend(y)
print(x)

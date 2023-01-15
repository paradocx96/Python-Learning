x = {"apple", "banana", "cherry", "apple"}
# cannot have duplicates
print(x)
print(len(x))
print(type(x))

x = {"apple", "banana", "cherry", 5200, 56.548}
print(x)

x = set(("apple", "banana", "cherry"))
print(x)

x = {"apple", "banana", "cherry", 5200, 56.548}
for i in x:
    print(i, end=' ')

print('\n')
print('apple' in x)

x.add('orange')
print(x)

x.update({'orange', 'mango', 'grapes'})
print(x)

x.update([25, 36, 48])
print(x)

# Remove
x.remove('banana')
print(x)

x.discard('orange')
print(x)

x.pop()
print(x)

x.clear()
print(x)

# del x
# print(x)

# Joining
x = {"apple", "banana", "cherry"}
y = {1, 2, 3}
z = x.union(y)
print(z)  # {1, 2, 'banana', 3, 'cherry', 'apple'}

x = {"apple", "banana", "cherry"}
y = {"apple", "melon", "mango"}
x.intersection_update(y)
print(x)  # {'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)  # {'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)  # {'cherry', 'microsoft', 'banana', 'google'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)  # {'cherry', 'microsoft', 'banana', 'google'}

x = {'id': 1, 'level': 2.354, 'said': "hello", "id": 2}
# duplicate keys are allowed
print(x)
print(len(x))
print(type(x))

print(x['id'])
print(x['level'])
print(x['said'])
print(x.get('id'))
print(x.keys())
print(x.values())
print(x.items())

for i in x:
    print(i, end=' ')

print('\n')

for key in x.keys():
    print(key, end=' ')

print('\n')

for value in x.values():
    print(value, end=' ')

print('\n')

for key, value in x.items():
    print(key, value, end=' - ')

print('\n')

# Change
x['id'] = 3
print(x)

x.update({'id': 5200})
print(x)

# Adding
x['new'] = 100
print(x)

# Removing
x.pop('new')
print(x)

x.popitem()
print(x)

del x['id']
print(x)

x.clear()
print(x)

# del x
# print(x)

# Copy
x = {'id': 1, 'level': 2.354, 'said': "hello"}
y = x.copy()
print(y)

y = dict(x)
print(y)

# Nested
x = {'id': 1, 'name': 'one'}
y = {'id': 2, 'name': 'two'}
z = {'id': 3, 'name': 'three'}
my_dict = {'x': x, 'y': y, 'z': z}
print(my_dict)

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# str
x = "Hello World"
y = str("Hello World")
print(type(x))
print(type(y))

# int
x = 20
y = int(20)
print(type(x))
print(type(y))

# float
x = 20.5
y = float(20.5)
print(type(x))
print(type(y))

# complex
x = 4123131j
y = complex(4123131j)
print(type(x))
print(type(y))

# list
x = ["apple", "banana", "cherry"]
y = list(("apple", "banana", "cherry"))
print(type(x))
print(type(y))

# tuple
x = ("apple", "banana", "cherry")
y = tuple(("apple", "banana", "cherry"))
print(type(x))
print(type(y))

# range
x = range(6)
print(type(x))

# dict
x = {"name": "John", "age": 36}
y = dict(name="John", age=36)
print(type(x))
print(type(y))

# set
x = {"apple", "banana", "cherry"}
y = set(("apple", "banana", "cherry"))
print(type(x))
print(type(y))

# frozenset
x = frozenset({"apple", "banana", "cherry"})
print(type(x))

# bool
x = True
y = bool(10)
print(type(x))
print(type(y))

# bytes
x = b"Hello"
y = bytes("Hello", "utf-8")
print(type(x))
print(type(y))

# bytearray
x = bytearray(5)
print(type(x))

# memoryview
x = memoryview(bytes(5))
print(type(x))

# NoneType
x = None
print(type(x))

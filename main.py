# Variables
x = 5
y = "USA"

# Print
print("X is", x)
print("Y is", y)

x = str(5200)
y = int(5200)
z = float(5200)

"""
Print variables
Print variable types
"""
print(x, y, z)
print(type(x), type(y), type(z))

x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

x = y = z = "Same Values"
print(x, y, z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

# Global variable
x = "awesome"


def print_x():
    x = "fantastic"
    print("Python is " + x)


def assign_global_value():
    global x
    x = "nice"
    print("Python is " + x)


print_x()
assign_global_value()
print("Python is " + x)

x = "Hello World"
print("X says: ", x)
print("X type: ", type(x))

# multiple lines string ("""xxx"""/'''xxx''')
x = """Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use 
of significant indentation. Python is dynamically-typed and 
garbage-collected. It supports multiple programming paradigms, 
including structured, object-oriented and functional programming
"""
print("X says: ", x)
print("X type: ", type(x))

# string as array
x = "Hello World"
print(x[6])

for i in x:
    print(i, end='')

print(len(x))

print("llo" in x)

print("llo" not in x)

print(x[2:8])

print(x[:8])

print(x[2:])

print(x[-5:-1])

print(x.upper())

print(x.lower())

x = "   Hello World   "
print(x.strip())

x = "Hello World"
print(x.replace("o", "8"))

x = "Hello World this is a string"
print(x.split(" "))

x = "Hello World"
y = "this is a string"
z = x + " " + y
print(z)

x = "World"
y = "string"
z = 2023
modified = "Hello {} This is a {} & {}"
print(modified.format(x, y, z))

modified = "Hello {2} This is a {0} & {1}"
print(modified.format(y, z, x))

x = "Hello World this\'s a string"
print(x)

x = "Hello World \\ this is a string"
print(x)

x = "Hello World \n this is a string"
print(x)

x = "Hello World \r this is a string"
print("Carriage Return ", x)

x = "Hello World \t this is a string"
print(x)

x = "Hello World \b this is a string"
print(x)

x = "Hello World \f this is a string"
print(x)

x = "Hello World \v this is a string"
print(x)

x = "Hello World \350 this is a string"
print(x)

# String Methods
x = "hello world"

print("Capitalize ", x.capitalize())
print("Casefold ", x.casefold())
print("Center ", x.center(25))
print("Count ", x.count("o"))
print("Encode ", x.encode())
print("Endswith ", x.endswith("d"))
print("Expandtabs ", x.expandtabs(1))
print("Find ", x.find("o"))
print("Format ", x.format())
print("Format_map ", x.format_map("o"))
print("Index ", x.index("o"))
print("Isalnum ", x.isalnum())
print("Isalpha ", x.isalpha())
print("Isdecimal ", x.isdecimal())
print("Isdigit ", x.isdigit())
print("Isidentifier ", x.isidentifier())
print("Islower ", x.islower())
print("Isnumeric ", x.isnumeric())
print("Isprintable ", x.isprintable())
print("Isspace ", x.isspace())
print("Istitle ", x.istitle())
print("Isupper ", x.isupper())
print("Join ", x.join("o"))
print("Ljust ", x.ljust(25))
print("Lower ", x.lower())
print("Lstrip ", x.lstrip())


try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")

try:
    print("Hello World")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# x = "hello world"
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")

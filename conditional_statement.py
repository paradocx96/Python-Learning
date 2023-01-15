x = 100
y = 500
z = 1000

if x > y:
    print("x is greater than y")
elif x == z:
    print("x is equal to y")
else:
    print("y is greater than x")

if y > x: print("y is greater than x")

print("x") if x > y else print("y")

if x > y and z > y:
    print("x and z is greater than y")
elif x > y or z > y:
    print("x or z is greater than y")

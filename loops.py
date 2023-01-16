i = 1

while i <= 10:
    print(i, end=' ')
    i += 1
    if i == 5:
        print("i is 5")
        continue
    elif i == 8:
        print("i is 8")
        break

print("\n")

while i >= 1:
    print(i, end=' ')
    i -= 1
else:
    print("i is 0")

# FOR
for x in "Hello World":
    print(x, end=' ')

print("\n")

x = ["banana", "apple", "cherry", "orange", "kiwi"]
for i in x:
    print(i)
    if i == "cherry":
        print("i is cherry")
        continue
    elif i == "orange":
        print("i is orange")
        break

for i in range(len(x)):
    print(i, end=' ')

print("\n")

for i in range(2, 10, 2):
    print(i, end=' ')
else:
    print("Finished")

# Nested Loops
for i in range(1, 6):
    for j in range(i):
        print("*", end=' ')
    print()

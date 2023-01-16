x = ["car", "bike", "truck"]
print(x[0])

x[2] = "bus"
print(x)

print(len(x))
print(type(x))

for i in x:
    print(i, end=" ")

print('\n')

x.append("train")
print(x)

x.pop(1)
print(x)

x.remove("bus")
print(x)

x.insert(1, "bus")
print(x)

x.reverse()
print(x)

x.sort()
print(x)

x.clear()
print(x)

import json

x = {
    "name": {
        "first": "John",
        "last": "Doe"
    },
    "age": 25,
    "married": False,
    "divorced": False,
    "children": False,
    "pets": ("dog", "cat"),
    "vehicles": [
        {"make": "Ford", "model": "F150", "year": 2015},
        {"make": "Honda", "model": "Accord", "year": 2012}
    ],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345",
        "country": "USA"
    },
}

y = json.dumps(x)
print(y)

y = json.dumps(x, indent=2)
print(y)

z = json.loads(y)
print(z["name"])
print(z["address"]["city"])

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

p = json.dumps(x, indent=2, separators=(". ", " = "))
print(p)

q = json.dumps(x, indent=2, sort_keys=True)
print(q)

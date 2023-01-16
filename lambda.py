# lambda arguments : expression

x = lambda a: a + 10
print(x(5))

x = lambda p, q: p * q
print(x(5, 6))


def new_func(n):
    return lambda a: a * n


print(new_func(2)(10))

func_result = new_func(2)
print(func_result(10))

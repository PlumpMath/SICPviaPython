def returnValue(func, x):
    return func(x)

def compose(f, g):
    return lambda x: f(g(x))

inc = lambda x: x + 1
square = lambda x: x ** 2

print(returnValue(compose(square, inc), 6))
# 49

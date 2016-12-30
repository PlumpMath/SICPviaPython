def returnValue(func, x):
    return func(x)

def compose(f, g):
    return lambda x: f(g(x))

def repeated(f, n):
    if n == 1:
        return f
    else:
        return compose(f, repeated(f, n - 1))

square = lambda x: x ** 2

print(returnValue(repeated(square, 2), 5))
# 625

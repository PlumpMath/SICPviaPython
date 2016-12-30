# Exercise-2.4
def cons(x, y):
    return lambda m: m(x, y)

def car(z):
    return z(lambda p, q: p)

def cdr(z):
    return z(lambda p, q: q)

# Exercise-2.5
def cons(a, b):
    return 2 ** a * 3 ** b

def car(z):
    if z % 2 != 0:
        return 0
    else:
        return car(z // 2) + 1

def cdr(z):
    if z % 3 != 0:
        return 0
    else:
        return cdr(z // 3) + 1

# Exercise-2.6
zero = lambda f: lambda x: x

def add_1(n):
    return lambda f: lambda x: f(n(f)(x))

one = lambda f: lambda x: f(x)

two = lambda f: lambda x: f(f(x))

def add(a, b):
    return lambda f: lambda x: a(f)(b(f)(x))

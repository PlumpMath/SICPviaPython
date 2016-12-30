def a(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return a((x - 1), a(x, (y - 1)))

print(a(1, 10))
# 1024
print(a(2, 4))
# 65536
print(a(3, 3))
# 65536

def f(n):
    return 2 * n

def g(n):
    return 2 ** n

def h(n):
    x = 1
    for i in range(n):
        x = 2 ** x
    return x

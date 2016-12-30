import sys
sys.setrecursionlimit(10000)

def cube(x):
    return x ** 3

def add(term, a, nextOne, b):
    if a > b:
        return 0
    else:
        return term(a) + add(term, nextOne(a), nextOne, b)

def simpson(f, a, b, n):
    h = (b - a) / n
    def y(k):
        return f(a + k * h)
    def factor(k):
        if k == 0 or k == n:
            return 1
        elif k % 2 != 0:
            return 4
        else:
            return 2
    def term(k):
        return factor(k) * y(k)
    def nextOne(k):
        return k + 1        
    return h / 3 * add(term, 0, nextOne, n)

print(simpson(cube, 0, 1, 100))
# 0.24999999999999992
print(simpson(cube, 0, 1, 1000))
# 0.2500000000000002

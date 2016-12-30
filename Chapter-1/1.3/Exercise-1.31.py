import sys
sys.setrecursionlimit(10000)

def productR(term, a, nextOne, b):
    if a > b:
        return 1
    else:
        return term(a) * productR(term, nextOne(a), nextOne, b)

def productI(term, a, nextOne, b):
    def productIter(a, result):
        if a > b:
            return result
        else:
            return product_iter(nextOne(a), term(a) * result)
    return productIter(a, 1)

def factorial(n):
    def identity(x):
        return x
    def inc(a):
        return a + 1
    return productR(identity, 1, inc, n)

def pi(n):
    def term(i):
        if i % 2 != 0:
            return (i + 1) / (i + 2)
        else:
            return (i + 2) / (i + 1)
    def inc(i):
        return i + 1
    return 4 * productR(term, 1, inc, n)

print(pi(10))
# 3.275101041334807
print(pi(100))
# 3.1570301764551645
print(pi(1000))
# 3.143160705532257

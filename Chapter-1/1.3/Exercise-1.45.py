from math import log2
TOLERANCE = 0.00001

def averageDamp(f):
    return lambda x: (x + f(x)) / 2

def compose(f, g):
    return lambda x: f(g(x))

def repeated(f, n):
    if n == 1:
        return f
    else:
        return compose(f, repeated(f, n - 1))

def nFoldAverageDamp(f, n):
    return (lambda g: g(f))(repeated(averageDamp, n))

def fixedPoint(f, firstGuess):
    def closeEnough(v1, v2):
        return abs(v2 - v1) < TOLERANCE
    def tryIt(guess):
        return (lambda nextOne: nextOne if closeEnough(guess, nextOne) else tryIt(nextOne))(f(guess))
    return tryIt(firstGuess)

def nRoot(x, n):
    print(fixedPoint(nFoldAverageDamp(lambda y: x / y ** (n - 1), int(log2(n))), 1.0))

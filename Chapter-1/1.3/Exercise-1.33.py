def filteredAccumulate(filt, combiner, nullValue, term, a, nextOne, b):
    def filteredTerm(n):
        if filt(n):
            return term(n)
        else:
            return nullValue
    if a > b:
        return nullValue
    else:
        return combiner(filteredTerm(a), filteredAccumulate(filt, combiner, nullValue, term, nextOne(a), next_a, b))

def prime(n):
    def findDivisor(n, testDivisor):
        if testDivisor ** 2 > n:
            return n
        elif n % testDivisor == 0:
            return testDivisor
        else:
            return findDivisor(n, testDivisor + 1)
    return n == findDivisor(n, 2)

def squareSumPrime(a, b):
    def inc(x):
        return x + 1
    def add(x, y):
        return x + y
    def square(x):
        return x ** 2
    return filteredAccumulate(prime, add, 0, square, a, inc, b)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def productRelativePrime(n):
    def relativePrime(a):
        return gcd(a, n) == 1
    def inc(x):
        return x + 1
    def multiply(x, y):
        return x * y
    def identity(x):
        return x
    return filteredAccumulate(relativePrime, multiply, 1, identity, 1, inc, n - 1)

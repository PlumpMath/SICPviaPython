# recursive:
def contFrac1(n, d, k):
    def cf(i):
        if i == k:
            return n(i) / d(i)
        else:
            return n(i) / (d(i) + cf(i + 1))
    return cf(1)

print(contFrac1(lambda i: 1.0, lambda i: 1.0, 11))
# 0.6180555555555556

# iterative:
def contFrac2(n, d, k):
    def cf(i, result):
        if i == 0:
            return result
        else:
            return cf(i - 1, n(i) / (d(i) + result))
    return cf(k, n(k) / d(k))

print(contFrac2(lambda i: 1.0, lambda i: 1.0, 11))
# 0.6180555555555556

def findK(tolerance, func):
    def enough(v1, v2):
        return abs(v1 - v2) < tolerance
    def tryIt(k):
        return (lambda nextOne: nextOne if enough(func(k),func(nextOne))
                else tryIt(nextOne))(k + 1)
    return tryIt(1)

print(findK(0.0001, lambda k: contFrac1(lambda i: 1.0, lambda i: 1.0, k)))
# 11

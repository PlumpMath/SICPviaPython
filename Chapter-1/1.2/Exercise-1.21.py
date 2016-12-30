def findDivisor(n, testDivisor):
    if testDivisor ** 2 > n:
        return n
    elif n % testDivisor == 0
        return testDivisor
    else:
        return findDivisor(n, testDivisor + 1)

def smallestDivisor(n):
    print(findDivisor(n, 2))

smallestDivisor(199)
# 199
smallestDivisor(1999)
# 1999
smallestDivisor(19999)
# 7

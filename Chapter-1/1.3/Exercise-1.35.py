TOLERANCE = 0.00001

def fixedPoint(f, firstGuess):
    def closeEnough(v1, v2):
        return abs(v1 - v2) < TOLERANCE
    def tryIt(guess):
        return (lambda nextOne: nextOne if closeEnough(guess, nextOne) else tryIt(nextOne))(f(guess))
    return tryIt(firstGuess)

print(fixedPoint(lambda x: 1 + 1 / x, 1.0))
# 1.6180327868852458

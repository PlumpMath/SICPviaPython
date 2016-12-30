from math import log

TOLERANCE = 0.00001

def fixedPoint(f, firstGuess):
    def closeEnough(v1, v2):
        return abs(v1 - v2) < TOLERANCE
    def tryIt(guess, step):
        return (lambda nextOne, step: print(nextOne, step) if closeEnough(guess, nextOne)
                else tryIt(nextOne, step + 1))(f(guess), step)
    tryIt(firstGuess, 1)

# without average damping:
fixedPoint(lambda x: log(1000) / log(x), 2.0)
# 4.555532270803653 34

def averageDamp(f):
    return lambda x: (x + f(x)) / 2

# with average damping:
fixedPoint(averageDamp(lambda x: log(1000) / log(x)), 2.0)
#4.555537551999825 9

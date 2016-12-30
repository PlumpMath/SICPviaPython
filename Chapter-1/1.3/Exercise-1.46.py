TOLERANCE = 0.0001

def iterativeImprove(goodEnough, improve):
    def tryIt(guess):
        return (lambda nextOne: nextOne if goodEnough(guess, nextOne) else tryIt(nextOne))(improve(guess))
    return lambda firstGuess: tryIt(firstGuess)

def sqrt(x):
    goodEnough = lambda v1, v2: abs(v2 - v1) < TOLERANCE
    improve = lambda guess: (guess + x / guess) / 2
    return iterativeImprove(goodEnough, improve)(1.0)

def fixedPoint(f, firstGuess):
    goodEnough = lambda v1, v2: abs(v2 - v1) < TOLERANCE
    improve = lambda guess: f(guess)
    return iterativeImprove(goodEnough, improve)(1.0)

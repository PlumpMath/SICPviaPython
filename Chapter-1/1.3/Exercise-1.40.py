TOLERANCE = 0.00001
DX = 0.00001

def fixedPoint(f, firstGuess):
	def closeEnough(v1, v2):
		return abs(v2 - v1) < TOLERANCE
	def tryIt(guess):
		return (lambda nextOne: nextOne if closeEnough(guess, nextOne) else tryIt(nextOne))(f(guess))
	return tryIt(firstGuess)

def deriv(g, x):
	return (g(x + DX) - g(x)) / DX

def newtonTransform(g):
	return lambda x: x - g(x) / deriv(g, x)
	
def newtonsMethod(g, guess):
	return fixedPoint(newtonTransform(g), guess)

def cubic(a, b, c):
	return lambda x: x ** 3 + a * x ** 2 + b * x + c

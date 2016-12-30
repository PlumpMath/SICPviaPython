# Exercise 1.6
def new_if(predicate, then_clause, else_clause):
    if predicate == True:
    	return then_clause
    else:
    	return else_clause

def sqrt(x):
    def improve(guess, x):
        return (guess + x / guess) / 2
    def good_enough(guess, x):
        return abs(guess ** 2 - x) < 0.001
    def sqrt_iter(guess, x):
        return new_if(good_enough(guess, x), guess, sqrt_iter(improve(guess, x), x))
    return sqrt_iter(1.0, x)
# RecursionError: maximum recursion depth exceeded in comparison

# Exercise 1.7
def sqrt(x):
    def improve(guess, x):
        return (guess + x / guess) / 2
    def good_enough(guess, guess_new):
        return (abs(guess_new - guess) / guess) < 0.001
    def sqrt_iter(guess, x):
        guess_new = improve(guess, x)
        if good_enough(guess, guess_new):
            return guess_new
        else:
            return sqrt_iter(guess_new, x)
    return sqrt_iter(1.0, x)

# Exercise 1.8
def cbrt(x):
    def improve(guess, x):
        return (x / guess ** 2 + 2 * guess) / 3
    def good_enough(guess, guess_new): 
        return (abs(guess_new - guess) / guess) < 0.001
    def cbrt_iter(guess,x):
        guess_new = improve(guess, x)
        if good_enough(guess, guess_new):
            return guess_new
        else:
            return cbrt_iter(guess_new, x)
    return cbrt_iter(1.0, x)

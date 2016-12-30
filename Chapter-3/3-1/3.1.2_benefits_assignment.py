from random import uniform
from sys import setrecursionlimit
setrecursionlimit(10000)

# Exercise 3.5
def monte_carlo(trials, experiment):
    def iter_monte_carlo(trials_remaining, trials_passed):
        if trials_remaining == 0:
            return trials_passed / trials
        elif experiment():
            return iter_monte_carlo(trials_remaining - 1, trials_passed + 1)
        else:
            return iter_monte_carlo(trials_remaining - 1, trials_passed)
    return iter_monte_carlo(trials, 0)

def estimate_integral(p, x1, x2, y1, y2, trials):
    return (x2 - x1) * (y2 - y1) * monte_carlo(trials, p)

def in_circle():
    return (uniform(-1, 1) ** 2 + uniform(-1, 1) ** 2) <= 1

estimate_pi = estimate_integral(in_circle, -1, 1, -1, 1, 5000)

print(estimate_pi)
# 3.152

# Exercise 3.6
def rand(symbol):
    if not hasattr(rand, "x"):
        rand.x = 1
    if symbol == "generate":
        rand.x = rand_update(rand.x)
        return rand.x
    elif symbol == "reset":
        def new_func(new_value):
            rand.x = new_value
        return new_func
    else:
        raise Exception("Unknown request -- RAND")

def double(x):
    return x + x

def halve(x):
    return x / 2

def multi(a, b):
    if b == 0:
        return 0
    elif b % 2 == 0:
        return multi(double(a), halve(b))
    else:
        return a + multi(a, b - 1)

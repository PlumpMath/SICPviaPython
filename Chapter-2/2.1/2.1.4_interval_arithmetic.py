from scheme_primitive import *

# Exercise-2.7
def make_interval(a, b):
    return cons(a, b)

def lower_bound(x):
    return car(x)

def upper_bound(x):
    return cdr(x)

# Exercise-2.8
def add_interval(x, y):
    return make_interval(lower_bound(x) + lower_bound(y), upper_bound(x) + upper_bound(y))

def sub_interval(x, y):
    return make_interval(lower_bound(x) - upper_bound(y), upper_bound(x) - lower_bound(y))

# Exercise-2.9
def width_interval(x):
    return (upper_bound(x) - lower_bound(x)) / 2

def width_add_or_sub_interval(x, y):
    return width_interval(x) + width_interval(y)

# Exercise-2.10
def mul_interval(x, y):
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_Bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    if lower_bound(y) * upper_bound(y) > 0:
        return mul_interval(x, make_interval(1.0 / upper_bound(y), 1.0 / lower_bound(y)))
    else:
        raise ZeroDivisionError("The denominator should not span 0.")

# Exercise-2.11
def sign_interval(x):
    if lower_bound(x) >= 0:
        return 1
    elif lower_bound(x) * upper_bound(x) < 0:
        return 0
    else:
        return -1

def mul_interval(x, y):
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    sx = sign_interval(x)
    sy = sign_interval(y)
    if sx == 1 and sy == 1:
        return make_internal(p1, p4)
    elif sx == 1 and sy == -1:
        return make_internal(p3, p2)
    elif sx == -1 and sy == 1:
        return make_internal(p2, p3)
    elif sx == -1 and sy == -1:
        return make_internal(p4, p1)
    elif sx == 0 and sy == 1:
        return make_internal(p2, p4)
    elif sx == 0 and sy == -1:
        return make_internal(p3, p1)
    elif sx == 1 and sy == 0:
        return make_internal(p3, p4)
    elif sx == -1 and sy == 0:
        return make_internal(p2, p1)
    else:
        return make_internal(min(p2, p3), max(p1, p4))

# Exercise-2.12
def make_center_percent(c, p):
    return make_interval(c * (1 - p / 100), c * (1 + p / 100))

def center(i):
    return (lower_bound(i) + upper_bound(i)) / 2

def percent(i):
    return 100 * width_interval(i) / center(i)

# Exercise-2.13
def percent_mul_interval(x, y):
    return percent(x) + percent(y)

# Exercise-2.14
def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = make_interval(1, 1)
    return div_interval(one, add_interval(div_interval(one, r1), div_interval(one, r2)))

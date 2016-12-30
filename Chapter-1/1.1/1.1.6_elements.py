# Exercise 1.1
print(10)
# 10

print(5 + 3 + 4)
# 12

print(9 - 1)
# 8

print(6 / 2)
# 3.0

print((2 * 4) + (4 - 6))
# 6

a = 3

b = a + 1

print(a + b + a * b)
# 19

print(a == b)
# False

if b > a and b < a * b:
    print(b)
else:
    print(a)
# 4

if a == 4:
    print(6)
elif b == 4:
    print(6 + 7 + a)
else:
    print(25)
# 16

print(2 + (b if b > a else a))
# 6

print((a if a > b else b if a < b else -1) * (a + 1))
# 16

# Exercise 1.2
print((5 + 4 + (2 - (3 - (6 + 4 / 5)))) / (3 * (6 - 2) * (2 - 7)))
# -0.24666666666666667

# Exercise 1.3
def larger(x, y):
    if x >= y:
        return x
    else:
        return y

def sum_square(x, y):
    return x ** 2 + y ** 2

def my_func(x, y, z):
    if x == larger(x, y):
        return sum_square(x, larger(y, z))
    else:
        return sum_square(y, larger(x, z))

# Exercise 1.4
def a_plus_abs_b(a, b):
    if b > 0:
        return a + b
    else:
        return a - b
# a plus the absolute value of b 

# Exercise 1.5
def p():
    return p()

def test(x, y):
    if x == 0:
        return 0
    else:
        return y

print(test(0, p()))
# RecursionError: maximum recursion depth exceeded
# Applicative-order is used, The evalution never stops.

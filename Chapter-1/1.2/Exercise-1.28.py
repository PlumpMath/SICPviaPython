import random
import sys
sys.setrecursionlimit(10000)

def even(n):
    return n % 2 == 0

def nontrivial_square_root(a, n):
    return a != 1 and a != n - 1 and a ** 2 % n == 1

def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif nontrivial_square_root(base, m):
        return 0
    elif even(exp):
        return expmod(base, exp / 2, m) ** 2 % m
    else:
        return base * expmod(base, exp - 1, m) % m

def Miller_Rabin_test(n):
    def try_it(a):
        return expmod(a, n - 1, n) == 1
    return try_it(random.randint(1, n - 1))

def test_iter(n, times):
    if times == 0:
        return True
    elif Miller_Rabin_test(n):
        return test_iter(n, times - 1)
    else:
        return False

def prime(n):
    print(test_iter(n, n // 2 + 1))

prime(561)
# False
prime(1105)
# False
prime(1729)
# False
prime(2465)
# False
prime(2821)
# False
prime(6601)
# False

prime(1009)
# True
prime(1013)
# True
prime(1019)
# True
prime(10007)
# True
prime(10009)
# True
prime(10037)
# True

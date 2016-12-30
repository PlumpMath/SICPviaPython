from datetime import datetime
import random
import sys
sys.setrecursionlimit(1000000)

def even(n):
    return n % 2 == 0

def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif even(exp):
        return expmod(base, exp / 2, m) ** 2 % m
    else:
        return base * expmod(base, exp - 1, m) % m

def fermat_test(n):
    def try_it(a):
        return expmod(a, n, n) == a
    return try_it(random.randint(1, n - 1))

def fast_prime(n, times):
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False

def timed_prime_test(n):
    print("\n", n, sep = "", end = "")
    start_time = datetime.now().microsecond
    if fast_prime(n, 1000):
        elapsed_time = datetime.now().microsecond - start_time
        print(" ***", elapsed_time, end = "")
        return True

timed_prime_test(1009)
timed_prime_test(1013)
timed_prime_test(1019)
timed_prime_test(10007)
timed_prime_test(10009)
timed_prime_test(10037)
timed_prime_test(100003)
timed_prime_test(100019)
timed_prime_test(100043)
timed_prime_test(1000003)
timed_prime_test(1000033)
timed_prime_test(1000037)

from datetime import datetime
import sys
sys.setrecursionlimit(1000000)

def divides(a, b):
    return b % a == 0

def find_divisor(n, test_divisor):
    if test_divisor ** 2 > n:
        return n
    elif divides(test_divisor, n):
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)

def smallest_divisor(n):
    return find_divisor(n, 2)

def prime(n):
    return n == smallest_divisor(n)

def timed_prime_test(n):
    print("\n", n, sep = "", end = "")
    start_time = datetime.now().microsecond
    if prime(n):
        elapsed_time = datetime.now().microsecond - start_time
        print(" ***", elapsed_time, end = "")
        return True

def search_for_primes(n, count):
    if n % 2 == 0:
        return search_for_primes(n + 1, count)
    elif count > 0:
        if timed_prime_test(n):
            return search_for_primes(n + 2, count - 1)
        else:
            return search_for_primes(n + 2, count)

search_for_primes(1000, 3)
# 1009, 1013, 1019
search_for_primes(10000, 3)
# 10007, 10009, 10037
search_for_primes(100000, 3)
# 100003, 100019, 100043
search_for_primes(1000000, 3)
# 1000003, 1000033, 1000037

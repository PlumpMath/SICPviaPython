from datetime import datetime
import sys
sys.setrecursionlimit(1000000)

def divides(a, b):
    return b % a == 0

def next_test_divisor(test_divisor):
    if test_divisor == 2:
        return 3
    else:
        return test_divisor + 2

def find_divisor(n, test_divisor):
    if test_divisor ** 2 > n:
        return n
    elif divides(test_divisor, n):
        return test_divisor
    else:
        return find_divisor(n, next_test_divisor(test_divisor))

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

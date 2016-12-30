import sys
sys.setrecursionlimit(7000)

def even(n):
    return n % 2 == 0

def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif even(exp):
        return expmod(base, exp / 2, m) ** 2 % m
    else:
        return base * expmod(base, exp - 1, m) % m

def fermat_test(n, a):
    return expmod(a, n, n) == a

def test_iter(n, i):
    if i == n:
        return True
    elif fermat_test(n, i):
        return test_iter(n, i + 1)
    else:
        return False

def carmichael(n):
    print(test_iter(n, 2))

carmichael(561)
# True
carmichael(1105)
# True
carmichael(1729)
# True
carmichael(2465)
# True
carmichael(2821)
# True
carmichael(6601)
# True

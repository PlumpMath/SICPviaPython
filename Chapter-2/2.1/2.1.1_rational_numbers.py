from scheme_primitive import *
from fractions import gcd

def make_rat(n, d):
    g = gcd(n, d)
    if d < 0:
        return cons(-n // g, -d // g)
    else:
        return cons(n // g, d // g)

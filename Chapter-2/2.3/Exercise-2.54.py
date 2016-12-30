# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

# Lists equal?
def equal(p1, p2):
    if p1 == None and p2 == None:
        return True
    elif p1 == None or p2 == None:
        return False
    elif callable(p1) and callable(p2):
        return equal(car(p1), car(p2)) and equal(cdr(p1), cdr(p2))
    elif callable(p1) or callable(p2):
        return False
    else:
        return p1 == p2

print(equal(makeList("this", "is", "a", "list"), makeList("this", "is", "a", "list")))
# True
print(equal(makeList("this", "is", "a", "list"), makeList("this", makeList("is", "a"), "list")))
# False

# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

# Set operations
def elementOfSet(x, set1):
    if set1 == None:
        return False
    elif x == car(set1):
        return True
    elif x < car(set1):
        return False
    else:
        return elementOfSet(x, cdr(set1))

def adjoinSet(x, set1):
    if set1 == None:
        return cons(x1, None)
    elif x == car(set1):
        return set1
    elif x < car(set1):
        return cons(x, set1)
    else:
        return cons(car(set1), adjoinSet(x, cdr(set1)))

def intersectionSet(set1, set2):
    if set1 == None or set2 == None:
        return None
    else:
        x1 = car(set1)
        x2 = car(set2)
        if x1 == x2:
            return cons(x1, intersectionSet(cdr(set1), cdr(set2)))
        elif x1 < x2:
            return cons(car(set1), intersectionSet(cdr(set1), set2))
        else:
            return intersectionSet(set1, cdr(set2))

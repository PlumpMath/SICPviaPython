# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

# Set operations
def unionSet(set1, set2):
    if set1 == None:
        return set2
    elif set2 == None:
        return set1
    else:
        x1 = car(set1)
        x2 = car(set2)
        if x1 == x2:
            return cons(x1, unionSet(cdr(set1), cdr(set2)))
        elif x1 < x2:
            return cons(x1, unionSet(cdr(set1), set2))
        else:
            return cons(x2, unionSet(set1, cdr(set2)))

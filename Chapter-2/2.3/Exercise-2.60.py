# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
appendList = lambda list1, list2: list2 if list1 == None else cons(car(list1), appendList(cdr(list1), list2))

# Set operations
def elementOfSet(x, set1):
    if set1 == None:
        return False
    elif x == car(set1):
        return True
    else:
        return elementOfSet(x, cdr(set1))

def adjoinSet(x, set1):
    if elementOfSet(x, set1):
        return set1
    else:
        return cons(x, set1)

def unionSet(set1, set2):
    return appendList(set1, set2)

def intersectionSet(set1, set2):
    if set1 == None or set2 == None:
        return None
    elif elementOfSet(car(set1), set2):
        return cons(car(set1), intersectionSet(cdr(set1), set2))
    else:
        return intersectionSet(cdr(set1), set2)

# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
cadr = lambda x: car(cdr(x))
caddr = lambda x: car(cdr(cdr(x)))
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

# Representation of binary trees
def entry(tree):
    return car(tree)

def leftBranch(tree):
    return cadr(tree)

def rightBranch(tree):
    return caddr(tree)

def makeTree(entry, left, right):
    return makeList(entry, left, right)

# Lookup procedure
def lookup(givenKey, setOfRecords):
    if setOfRecords == None:
        return False
    else:
        x = key(entry(setOfRecords))
        if givenKey == x:
            return entry(setOfRecords)
        elif x < givenKey:
            return lookup(givenKey, leftBranch(setOfRecords))
        else:
            return lookup(givenKey, rightBranch(setOfRecords))

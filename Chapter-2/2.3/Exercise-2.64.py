# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
listLength = lambda items: 0 if items == None else 1 + listLength(cdr(items))

# Representation of binary trees
def entry(tree):
    return car(tree)

def leftBranch(tree):
    return cadr(tree)

def rightBranch(tree):
    return caddr(tree)

def makeTree(entry, left, right):
    return makeList(entry, left, right)

# List to tree
def listToTree(elements):
    return car(partialTree(elements, listLength(elements)))

def partialTree(elts, n):
    if n == 0:
        return cons(None, elts)
    else:
        leftSize = (n - 1) // 2
        leftResult = partialTree(elts, leftSize)
        leftTree = car(leftResult)
        nonLeftElts = cdr(leftResult)
        rightSize = n - (leftSize + 1)
        thisEntry = car(nonLeftElts)
        rightResult = partialTree(cdr(nonLeftElts), rightSize)
        rightTree = car(rightResult)
        remainingElts = cdr(rightResult)
        return cons(makeTree(thisEntry, leftTree, rightTree), remainingElts)
        
# Order of growth: O(n)

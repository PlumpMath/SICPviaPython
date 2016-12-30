# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
cadr = lambda x: car(cdr(x))
caddr = lambda x: car(cdr(cdr(x)))
cadddr = lambda x: car(cdr(cdr(cdr(x))))
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
appendList = lambda list1, list2: list2 if list1 == None else cons(car(list1), appendList(cdr(list1), list2))

def printList(items):
    displayList = lambda items: '[' + displayItems(items) + ']' 
    displayItems = lambda items: displayItem(car(items)) if cdr(items) == None \
                   else displayItem(car(items)) + ', ' + displayItem(cdr(items)) if not callable(cdr(items)) \
                   else displayItem(car(items)) + ', ' + displayItems(cdr(items))
    displayItem = lambda item: '[]' if item == None \
                  else str(item) if not callable(item) \
                  else displayList(item)
    print(displayList(items))

# Representation of leaf
def makeLeaf(symbol, weight):
    return makeList("leaf", symbol, weight)

def isLeaf(item):
    return car(item) == "leaf"

def symbolLeaf(x):
    return cadr(x)

def weightLeaf(x):
    return caddr(x)

# Representation of tree
def makeCodeTree(left, right):
    return makeList(left, right, appendList(symbols(left), symbols(right)), (weight(left) + weight(right)))

def leftBranch(tree):
    return car(tree)

def rightBranch(tree):
    return cadr(tree)

def symbols(tree):
    if isLeaf(tree):
        return makeList(symbolLeaf(tree))
    else:
        return caddr(tree)

def weight(tree):
    if isLeaf(tree):
        return weightLeaf(tree)
    else:
        return cadddr(tree)

# Encode
def elementOfSet(x, set1):
    if set1 == None:
        return False
    elif x == car(set1):
        return True
    else:
        return elementOfSet(x, cdr(set1))

def encode(message, tree):
    if message == None:
        return None
    else:
        return appendList(encodeSymbol(car(message), tree), encode(cdr(message), tree))

def encodeSymbol(symbol, tree):
    def goodBranch(branch):
        if isLeaf(branch):
            return symbol == symbolLeaf(branch)
        else:
            return elementOfSet(symbol, symbols(branch))
    lb = leftBranch(tree)
    rb = rightBranch(tree)
    if goodBranch(lb):
        if isLeaf(lb):
            return makeList(0)
        else:
            return cons(0, encodeSymbol(symbol, lb))
    elif goodBranch(rb):
        if isLeaf(rb):
            return makeList(1)
        else:
            return cons(1, encodeSymbol(symbol, rb))
    else:
        raise Exception("bad symbol -- ENCODE-SYMBOL")

sampleTree = makeCodeTree(makeLeaf("A", 4), makeCodeTree(makeLeaf("B", 2), makeCodeTree(makeLeaf("D", 1), makeLeaf("C", 1))))
sampleMessage = makeList("A", "D", "A", "B", "B", "C", "A")

printList(encode(sampleMessage, sampleTree))
# [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]

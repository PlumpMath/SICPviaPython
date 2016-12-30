# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
cadr = lambda x: car(cdr(x))
caddr = lambda x: car(cdr(cdr(x)))
cadddr = lambda x: car(cdr(cdr(cdr(x))))
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
appendList = lambda list1, list2: list2 if list1 == None else cons(car(list1), appendList(cdr(list1), list2))

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

# Generate Huffman tree
def adjoinSet(x, set1):
    if set1 == None:
        return makeList(x)
    elif weight(x) < weight(car(set1)):
        return cons(x, set1)
    else:
        return cons(car(set1), adjoinSet(x, cdr(set1)))

def makeLeafSet(pairs):
    if pairs == None:
        return None
    else:
        pair = car(pairs)
        return adjoinSet(makeLeaf(car(pair), cadr(pair)), makeLeafSet(cdr(pairs)))

def successiveMerge(leafSet):
    if cdr(leafSet) == None:
        return car(leafSet)
    else:
        return successiveMerge(adjoinSet(makeCodeTree(car(leafSet), cadr(leafSet)), cddr(leafSet)))

def generateHuffmanTree(pairs):
    return successiveMerge(makeLeafSet(pairs))

# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
cadr = lambda x: car(cdr(x))
caddr = lambda x: car(cdr(cdr(x)))
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
appendList = lambda list1, list2: list2 if list1 == None else cons(car(list1), appendList(cdr(list1), list2))
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

# Tree to list
def treeToList(tree):
    def copyToList(tree, resultList):
        if tree == None:
            return resultList
        else:
            return copyToList(leftBranch(tree), cons(entry(tree), copyToList(rightBranch(tree), resultList)))
    return copyToList(tree, None)

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

# Tree operation
def unionSet(set1, set2):
    def unionList(list1, list2):
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            x1 = car(list1)
            x2 = car(list2)
            if x1 == x2:
                return cons(x1, unionList(cdr(list1), cdr(list2)))
            elif x1 < x2:
                return cons(x1, unionList(cdr(list1), list2))
            else:
                return cons(x2, unionList(list1, cdr(list2)))
    return listToTree(unionList(treeToList(set1), treeToList(set2)))

def intersectionSet(set1, set2):
    def intersectionList(list1, list2):
        if list1 == None or list2 == None:
            return None
        else:
            x1 = car(list1)
            x2 = car(list2)
            if x1 == x2:
                return cons(x1, intersectionList(cdr(set1), cdr(set2)))
            elif x1 < x2:
                return cons(car(set1), intersectionList(cdr(set1), set2))
            else:
                return intersectionList(set1, cdr(set2))
    return listToTree(intersectionList(treeToList(set1), treeToList(set2)))

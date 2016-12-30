# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
cadr = lambda x: car(cdr(x))
caddr = lambda x: car(cdr(cdr(x)))
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
def treeToList1(tree):
    if tree == None:
        return None
    else:
        return appendList(treeToList1(leftBranch(tree)), cons(entry(tree), treeToList1(rightBranch(tree))))

def treeToList2(tree):
    def copyToList(tree, resultList):
        if tree == None:
            return resultList
        else:
            return copyToList(leftBranch(tree), cons(entry(tree), copyToList(rightBranch(tree), resultList)))
    return copyToList(tree, None)

printList(treeToList1(makeTree(7, makeTree(3, makeTree(1, None, None), makeTree(5, None, None)), makeTree(9, None, makeTree(11, None, None)))))
# [1, 3, 5, 7, 9, 11]
printList(treeToList1(makeTree(3, makeTree(1, None, None), makeTree(7, makeTree(5, None, None), makeTree(9, None, makeTree(11, None, None))))))
# [1, 3, 5, 7, 9, 11]
printList(treeToList1(makeTree(5, makeTree(3, makeTree(1, None, None), None), makeTree(9, makeTree(7, None, None), makeTree(11, None, None)))))
# [1, 3, 5, 7, 9, 11]
# Order of growth: O(nlogn)

printList(treeToList2(makeTree(7, makeTree(3, makeTree(1, None, None), makeTree(5, None, None)), makeTree(9, None, makeTree(11, None, None)))))
# [1, 3, 5, 7, 9, 11]
printList(treeToList2(makeTree(3, makeTree(1, None, None), makeTree(7, makeTree(5, None, None), makeTree(9, None, makeTree(11, None, None))))))
# [1, 3, 5, 7, 9, 11]
printList(treeToList2(makeTree(5, makeTree(3, makeTree(1, None, None), None), makeTree(9, makeTree(7, None, None), makeTree(11, None, None)))))
# [1, 3, 5, 7, 9, 11]
# Order of growth: O(n)

# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
mapList = lambda proc, items: None if items == None else cons(proc(car(items)), mapList(proc, cdr(items)))

def printList(items):
    displayList = lambda items: '[' + displayItems(items) + ']' 
    displayItems = lambda items: displayItem(car(items)) if cdr(items) == None \
                   else displayItem(car(items)) + ', ' + displayItem(cdr(items)) if not callable(cdr(items)) \
                   else displayItem(car(items)) + ', ' + displayItems(cdr(items))
    displayItem = lambda item: '[]' if item == None \
                  else str(item) if not callable(item) \
                  else displayList(item)
    print(displayList(items))

# Square tree
def squareTree1(tree):
    if tree == None:
        return None
    elif not callable(tree):
        return tree ** 2
    else:
        return cons(squareTree1(car(tree)), squareTree1(cdr(tree)))

printList(squareTree1(makeList(1, makeList(2, makeList(3, 4), 5), makeList(6, 7))))
# [1, [4, [9, 16], 25], [36, 49]]

def squareTree2(tree):
    return mapList(lambda subTree: subTree ** 2 if not callable(subTree) else squareTree2(subTree), tree)

printList(squareTree2(makeList(1, makeList(2, makeList(3, 4), 5), makeList(6, 7))))
# [1, [4, [9, 16], 25], [36, 49]]

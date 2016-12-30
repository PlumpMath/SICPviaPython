# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
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

# Deep reverse
def deepReverse(items):
    if items == None:
        return None
    elif callable(car(items)):
        return appendList(deepReverse(cdr(items)), makeList(deepReverse(car(items))))
    else:
        return appendList(deepReverse(cdr(items)), makeList(car(items)))

x = makeList(makeList(1, 2), makeList(3, 4))
printList(deepReverse(x))
# [[4, 3], [2, 1]]

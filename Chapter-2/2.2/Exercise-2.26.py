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

# Evaluate
x = makeList(1, 2, 3)
y = makeList(4, 5, 6)

printList(appendList(x, y))
# [1, 2, 3, 4, 5, 6] 
printList(cons(x, y))
# [[1, 2, 3], 4, 5, 6]
printList(makeList(x, y))
# [[1, 2, 3], [4, 5, 6]]

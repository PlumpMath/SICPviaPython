# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
mapList = lambda proc, items: None if items == None else cons(proc(car(items)), mapList(proc, cdr(items)))
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

# Subsets
def subsets(s):
    if s == None:
        return makeList(None)
    else:
        rest = subsets(cdr(s))
        return appendList(rest, mapList(lambda item: appendList(makeList(car(s)), item), rest))

printList(subsets(makeList(1, 2, 3)))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

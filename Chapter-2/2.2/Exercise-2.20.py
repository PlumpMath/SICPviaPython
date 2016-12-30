# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

def printList(items):
    displayList = lambda items: '[' + displayItems(items) + ']' 
    displayItems = lambda items: displayItem(car(items)) if cdr(items) == None \
                   else displayItem(car(items)) + ', ' + displayItem(cdr(items)) if not callable(cdr(items)) \
                   else displayItem(car(items)) + ', ' + displayItems(cdr(items))
    displayItem = lambda item: '[]' if item == None \
                  else str(item) if not callable(item) \
                  else displayList(item)
    print(displayList(items))

# Same parity
def sameParity(sample, *items):
    def sameParityIter(sample, myList):
        if myList == None:
            return None
        elif (car(myList) - sample) % 2 == 0:
            return cons(car(myList), sameParityIter(sample, cdr(myList)))
        else:
            return sameParityIter(sample, cdr(myList))
    return cons(sample, sameParityIter(sample, makeList(*items)))

printList(sameParity(1, 2, 3, 4, 5, 6, 7))
# [1, 3, 5, 7]
printList(sameParity(2, 3, 4, 5, 6, 7))
# [2, 4, 6] 

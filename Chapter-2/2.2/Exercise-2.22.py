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

# Square list
def squareList1(items):
    def squareListIter(things, answer):
        if things == None:
            return answer
        else:
            return squareListIter(cdr(things), cons(car(things) ** 2, answer))
    return squareListIter(items, None)

printList(squareList1(makeList(1, 2, 3, 4)))
# [16, 9, 4, 1]

def squareList2(items):
    def squareListIter(things, answer):
        if things == None:
            return answer
        else:
            return squareListIter(cdr(things), cons(answer, car(things) ** 2))
    return squareListIter(items, None)

printList(squareList2(makeList(1, 2, 3, 4)))
# [[[[[], 1], 4], 9], 16]

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

# Fold right & fold left
def foldLeft(op, initial, sequence):
    def foldLeftIter(result, rest):
        if rest == None:
            return result
        else:
            return foldLeftIter(op(result, car(rest)), cdr(rest))
    return foldLeftIter(initial, sequence)

def foldRight(op, initial, sequence):
    if sequence == None:
        return initial
    else:
        return op(car(sequence), foldRight(op, initial, cdr(sequence)))

print(foldRight(lambda x, y: x / y, 1, makeList(1, 2, 3)))
# 1.5
print(foldLeft(lambda x, y: x / y, 1, makeList(1, 2, 3)))
# 0.16666666666666666
printList(foldRight(makeList, None, makeList(1, 2, 3)))
# [1, [2, [3, []]]]
printList(foldLeft(makeList, None, makeList(1, 2, 3)))
# [[[[], 1], 2], 3]

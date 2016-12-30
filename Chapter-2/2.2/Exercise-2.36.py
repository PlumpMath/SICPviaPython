# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
accumulate = lambda op, initial, sequence: initial if sequence == None else op(car(sequence), accumulate(op, initial, cdr(sequence)))
mapList = lambda p, sequence: accumulate(lambda x, y: cons(p(x), y), None, sequence)

def printList(items):
    displayList = lambda items: '[' + displayItems(items) + ']' 
    displayItems = lambda items: displayItem(car(items)) if cdr(items) == None \
                   else displayItem(car(items)) + ', ' + displayItem(cdr(items)) if not callable(cdr(items)) \
                   else displayItem(car(items)) + ', ' + displayItems(cdr(items))
    displayItem = lambda item: '[]' if item == None \
                  else str(item) if not callable(item) \
                  else displayList(item)
    print(displayList(items))

# accumulate-n
def accumulateN(op, init, seqs):
    if car(seqs) == None:
        return None
    else:
        return cons(accumulate(op, init, mapList(car, seqs)), accumulateN(op, init, mapList(cdr, seqs)))

printList(accumulateN(lambda x, y: x + y, 0, makeList(makeList(1, 2, 3), makeList(4, 5, 6), makeList(7, 8, 9), makeList(10, 11, 12))))
# [22, 26, 30]

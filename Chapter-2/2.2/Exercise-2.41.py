# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
accumulate = lambda op, initial, sequence: initial if sequence == None else op(car(sequence), accumulate(op, initial, cdr(sequence)))
enumerateInterval = lambda low, high: None if low > high else cons(low, enumerateInterval(low + 1, high))
appendList = lambda list1, list2: accumulate(cons, list2, list1)
mapList = lambda p, sequence: accumulate(lambda x, y: cons(p(x), y), None, sequence)
flatMap = lambda proc, seq: accumulate(appendList, None, mapList(proc, seq))
filterList = lambda predicate, sequence: None if sequence == None \
             else cons(car(sequence), filterList(predicate, cdr(sequence))) if predicate(car(sequence)) \
             else filterList(predicate, cdr(sequence))

# ordered-triple sum
def listSum(sequence):
    return accumulate(lambda x, y: x + y, 0, sequence)

def orderedTriples(n):
    return flatMap(lambda i: flatMap(lambda j: mapList(lambda k: makeList(i, j, k),
                                                       enumerateInterval(1, j - 1)),
                                     enumerateInterval(1, i - 1)),
                   enumerateInterval(1, n))

def filteredOrderedTriples(n, s):
    return filterList(lambda sequence: listSum(sequence) == s, orderedTriples(n))

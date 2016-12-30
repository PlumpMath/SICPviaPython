# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
cadr = lambda pair: car(cdr(pair))
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
accumulate = lambda op, initial, sequence: initial if sequence == None else op(car(sequence), accumulate(op, initial, cdr(sequence)))
enumerateInterval = lambda low, high: None if low > high else cons(low, enumerateInterval(low + 1, high))
appendList = lambda list1, list2: accumulate(cons, list2, list1)
mapList = lambda p, sequence: accumulate(lambda x, y: cons(p(x), y), None, sequence)
flatMap = lambda proc, seq: accumulate(appendList, None, mapList(proc, seq))
filterList = lambda predicate, sequence: None if sequence == None \
             else cons(car(sequence), filterList(predicate, cdr(sequence))) if predicate(car(sequence)) \
             else filterList(predicate, cdr(sequence))

def printList(items):
    displayList = lambda items: '[' + displayItems(items) + ']' 
    displayItems = lambda items: displayItem(car(items)) if cdr(items) == None \
                   else displayItem(car(items)) + ', ' + displayItem(cdr(items)) if not callable(cdr(items)) \
                   else displayItem(car(items)) + ', ' + displayItems(cdr(items))
    displayItem = lambda item: '[]' if item == None \
                  else str(item) if not callable(item) \
                  else displayList(item)
    print(displayList(items))

# Prime-sum pairs
def prime(n):
    def findDivisor(n, testDivisor):
        if testDivisor ** 2 > n:
            return n
        elif n % testDivisor == 0:
            return testDivisor
        else:
            return findDivisor(n, testDivisor + 1)
    return n == findDivisor(n, 2)

def primeSum(pair):
    return prime(car(pair) + cadr(pair))

def makePairSum(pair):
    return makeList(car(pair), cadr(pair), car(pair) + cadr(pair))

def uniquePairs(n):
    return flatMap(lambda i: mapList(lambda j: makeList(i, j), enumerateInterval(1, i - 1)), enumerateInterval(1, n))

def primeSumPairs(n):
    return mapList(makePairSum, filterList(primeSum, uniquePairs(n)))

printList(primeSumPairs(6))
# [[2, 1, 3], [3, 2, 5], [4, 1, 5], [4, 3, 7], [5, 2, 7], [6, 1, 7], [6, 5, 11]]

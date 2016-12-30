# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
accumulate = lambda op, initial, sequence: initial if sequence == None else op(car(sequence), accumulate(op, initial, cdr(sequence)))
appendList = lambda list1, list2: accumulate(cons, list2, list1)

# Reverse
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

def reverseRight(sequence):
    return foldRight(lambda x, y: appendList(y, makeList(x)), None, sequence)

def reverseLeft(sequence):
    return foldLeft(lambda x, y: cons(y, x), None, sequence)

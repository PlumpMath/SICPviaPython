# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
accumulate = lambda op, initial, sequence: initial if sequence == None else op(car(sequence), accumulate(op, initial, cdr(sequence)))

# basic list-manipulation operations
def mapList(p, sequence):
    return accumulate(lambda x, y: cons(p(x), y), None, sequence)

def appendList(seq1, seq2):
    return accumulate(cons, seq2, seq1)

def length(sequence):
    return accumulate(lambda x, y: 1 + y, 0, sequence)

# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
accumulate = lambda op, initial, sequence: initial if sequence == None else op(car(sequence), accumulate(op, initial, cdr(sequence)))
accumulateN = lambda op, init, seqs: None if car(seqs) == None \
              else cons(accumulate(op, init, mapList(car, seqs)), accumulateN(op, init, mapList(cdr, seqs)))
mapList = lambda p, sequence: accumulate(lambda x, y: cons(p(x), y), None, sequence)
mapMultipleList = lambda p, *sequence: mapList(p, transpose(makeList(*sequence)))
listProduct = lambda seq: accumulate(lambda x, y: x * y, 1, seq)

# matrix algebra
def dotProduct(v, w):
    return accumulate(lambda x, y: x + y, 0, mapMultipleList(listProduct, v, w))

def matrixMulVector(m, v):
    return mapList(lambda w: dotProduct(v, w), m)

def transpose(mat):
    return accumulateN(cons, None, mat)

def matrixMulMatrix(m, n):
    cols = transpose(n)
    return mapList(lambda row: matrixMulVector(cols, row), m)

# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
accumulate = lambda op, initial, sequence: initial if sequence == None else op(car(sequence), accumulate(op, initial, cdr(sequence)))
mapList = lambda p, sequence: accumulate(lambda x, y: cons(p(x), y), None, sequence)
enumerateTree = lambda tree: None if tree == None else makeList(tree) if not callable(tree) \
                else appendList(enumerateTree(car(tree)), enumerateTree(cdr(tree)))

# Count leaves
def countLeaves(t):
    return accumulate(lambda x, y: x + y, 0, mapList(lambda x: 1, enumerateTree(t)))

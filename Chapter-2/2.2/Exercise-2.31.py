# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
mapList = lambda proc, items: None if items == None else cons(proc(car(items)), mapList(proc, cdr(items)))

# Tree map
def treeMap(proc, tree):
    return mapList(lambda subTree: proc(subTree) if not callable(subTree) else treeMap(proc, subTree), tree)

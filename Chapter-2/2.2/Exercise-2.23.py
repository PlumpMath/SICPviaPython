# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

# For-each
def forEach(proc, items):
    if items == None:
        pass
    else:
        proc(car(items))
        forEach(proc, cdr(items))

forEach(lambda x: print(x), makeList(57, 321, 88))
# 57
# 321
# 88

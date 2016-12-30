# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

# Frame constructor & selectors 1
def makeFrame(origin, edge1, edge2):
    return makeList(origin, edge1, edge2)

def frameOrigin(frame):
    return car(frame)

def frameEdge1(frame):
    return car(cdr(frame))

def frameEdge2(frame):
    return car(cdr(cdr(frame)))

# Frame constructor & selectors 2
def makeFrame(origin, edge1, edge2):
    return cons(origin, cons(edge1, edge2))

def frameOrigin(frame):
    return car(frame)

def frameEdge1(frame):
    return car(cdr(frame))

def frameEdge2(frame):
    return cdr(cdr(frame))

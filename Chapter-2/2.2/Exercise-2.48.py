# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)

# Segments constructor & selectors
def makeSegment(start, end):
    return cons(start, end)

def startSegment(segment):
    return car(segment)

def endSegment(segment):
    return cdr(segment)

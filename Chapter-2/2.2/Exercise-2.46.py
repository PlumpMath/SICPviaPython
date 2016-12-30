# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)

# Vector constructor & selectors
def makeVect(xcor, ycor):
    return cons(xcor, ycor)

def xcorVect(vect):
    return car(vect)

def ycorVect(vect):
    return cdr(vect)

# Vector operations
def addVect(vect1, vect2):
    return makeVect(xcorVect(vect1) + xcorVect(vect2), ycorVect(vect1) + ycorVect(vect2))

def subVect(vect1, vect2):
    return makeVect(xcorVect(vect1) - xcorVect(vect2), ycorVect(vect1) - ycorVect(vect2))

def scaleVect(s, vect):
    return makeVect(s * xcorVect(vect), s * ycorVect(vect))

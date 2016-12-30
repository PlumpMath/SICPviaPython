# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)

# Vector constructor & selectors
makeVect = lambda xcor, ycor: cons(xcor, ycor)
xcorVect = lambda vect: car(vect)
ycorVect = lambda vect: cdr(vect)

# Vector operations
addVect = lambda vect1, vect2: makeVect(xcorVect(vect1) + xcorVect(vect2), ycorVect(vect1) + ycorVect(vect2))
subVect = lambda vect1, vect2: makeVect(xcorVect(vect1) - xcorVect(vect2), ycorVect(vect1) - ycorVect(vect2))
scaleVect = lambda s, vect: makeVect(s * xcorVect(vect), s * ycorVect(vect))

# Frame constructor & selectors
makeFrame = lambda origin, edge1, edge2: cons(origin, cons(edge1, edge2))
frameOrigin = lambda frame: car(frame)
frameEdge1 = lambda frame: car(cdr(frame))
frameEdge2 = lambda frame: cdr(cdr(frame))

# Frame's coordinate map
def frameCoordMap(frame):
    return lambda v: addVect(frameOrigin(frame),
                             addVect(scaleVect(xcorVect(v), frameEdge1(frame)),
                                     scaleVect(ycorVect(v), frameEdge2(frame))))

# Painter transformation & combination
def transformPainter(painter, origin, corner1, corner2):
    def newPainter(frame):
        m = frameCoordMap(frame)
        newOrigin = (lambda f, x: f(x))(m, origin)
        painter(makeFrame(newOrigin, subVect(m(corner1), newOrigin), subVect(m(corner2), newOrigin)))
    return newPainter

def beside(painter1, painter2):
    splitPoint = makeVect(0.5, 0)
    paintLeft = transformPainter(painter1, makeVect(0, 0), splitPoint, makeVect(0, 1))
    paintRight = transformPainter(painter2, splitPoint, makeVect(1, 0), makeVect(0.5, 1))
    def newPainter(frame):
        paintLeft(frame)
        paintRight(frame)
    return newPainter 

def below(painter1, painter2):
    splitPoint = makeVect(0, 0.5)
    paintUp = transformPainter(painter1, makeVect(0, 0), makeVect(1, 0), splitPoint)
    paintDown = transformPainter(painter2, splitPoint, makeVect(1, 0.5), makeVect(0, 1))
    def newPainter(frame):
        paintUp(frame)
        paintDown(frame)
    return newPainter

def split(div1, div2):
    def newPainter(painter, n):
        if n == 0:
            return painter
        else:
            smaller = newPainter(painter, n - 1)
            return div1(painter, div2(smaller, smaller))
    return newPainter

rightSplit = split(beside, below)
upSplit = split(below, beside)

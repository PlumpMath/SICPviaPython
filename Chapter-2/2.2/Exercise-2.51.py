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

# Painter transformation
def transformPainter(painter, origin, corner1, corner2):
    def newPainter(frame):
        m = frameCoordMap(frame)
        newOrigin = (lambda f, x: f(x))(m, origin)
        painter(makeFrame(newOrigin, subVect(m(corner1), newOrigin), subVect(m(corner2), newOrigin)))
    return newPainter

def rotate90(painter):
    return transformPainter(painter, makeVect(1, 0), makeVect(1, 1), makeVect(0, 0))

def rotate270(painter):
    return transformPainter(painter, makeVect(0, 1), makeVect(0, 0), makeVect(1, 1))

# Painter combination
def beside(painter1, painter2):
    splitPoint = makeVect(0.5, 0)
    paintLeft = transformPainter(painter1, makeVect(0, 0), splitPoint, makeVect(0, 1))
    paintRight = transformPainter(painter2, splitPoint, makeVect(1, 0), makeVect(0.5, 1))
    def newPainter(frame):
        paintLeft(frame)
        paintRight(frame)
    return newPainter 

def below1(painter1, painter2):
    splitPoint = makeVect(0, 0.5)
    paintUp = transformPainter(painter1, makeVect(0, 0), makeVect(1, 0), splitPoint)
    paintDown = transformPainter(painter2, splitPoint, makeVect(1, 0.5), makeVect(0, 1))
    def newPainter(frame):
        paintUp(frame)
        paintDown(frame)
    return newPainter

def below2(painter1, painter2):
    return rotate90(beside(rotate270(painter1), rotate270(painter2)))

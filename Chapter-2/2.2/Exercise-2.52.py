# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

def forEach(proc, items):
    if items == None:
        pass
    else:
        proc(car(items))
        forEach(proc, cdr(items))

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

# Vector constructor & selectors
makeVect = lambda xcor, ycor: cons(xcor, ycor)
xcorVect = lambda vect: car(vect)
ycorVect = lambda vect: cdr(vect)

# Vector operations
addVect = lambda vect1, vect2: makeVect(xcorVect(vect1) + xcorVect(vect2), ycorVect(vect1) + ycorVect(vect2))
subVect = lambda vect1, vect2: makeVect(xcorVect(vect1) - xcorVect(vect2), ycorVect(vect1) - ycorVect(vect2))
scaleVect = lambda s, vect: makeVect(s * xcorVect(vect), s * ycorVect(vect))

# Segments constructor & selectors
makeSegment = lambda start, end: cons(start, end)
startSegment = lambda segment: car(segment)
endSegment = lambda segment: cdr(segment)
def segmentsPainter(segmentList):
    return lambda frame: forEach(lambda segment: drawLine((lambda f, x: f(x))(frameCoordMap(frame), startSegment(segment)),
                                                          (lambda f, x: f(x))(frameCoordMap(frame), endSegment(segment))),
                                 segmentList)

# primitive picture language procedures
from PIL import Image, ImageDraw, ImageOps
IMAGE_SIZE = (500, 500)

im1 = Image.new("RGB", IMAGE_SIZE, "white")
draw = ImageDraw.Draw(im1)

def drawLine(vect1, vect2):
    draw.line([(xcorVect(vect1), ycorVect(vect1)), (xcorVect(vect2), ycorVect(vect2))], fill = 0)

painterWave = segmentsPainter(makeList(makeSegment(makeVect(0, 0.85), makeVect(0.15, 0.6)),
                                       makeSegment(makeVect(0, 0.65), makeVect(0.15, 0.4)),
                                       makeSegment(makeVect(0.3, 0.65), makeVect(0.15, 0.6)),
                                       makeSegment(makeVect(0.3, 0.6), makeVect(0.15, 0.4)),
                                       makeSegment(makeVect(0.3, 0.65), makeVect(0.4, 0.65)),
                                       makeSegment(makeVect(0.3, 0.6), makeVect(0.35, 0.5)),
                                       makeSegment(makeVect(0.4, 0.65), makeVect(0.35, 0.85)),
                                       makeSegment(makeVect(0.35, 0.5), makeVect(0.25, 0)),
                                       makeSegment(makeVect(0.4, 0), makeVect(0.5, 0.3)),
                                       makeSegment(makeVect(0.5, 0.3), makeVect(0.6, 0)),
                                       makeSegment(makeVect(0.4, 0), makeVect(0.5, 0.3)),
                                       makeSegment(makeVect(0.5, 0.3), makeVect(0.6, 0)),
                                       makeSegment(makeVect(0.35, 0.85), makeVect(0.4, 1)),
                                       makeSegment(makeVect(0.6, 1), makeVect(0.65, 0.85)),
                                       makeSegment(makeVect(0.65, 0.85), makeVect(0.6, 0.65)),
                                       makeSegment(makeVect(0.6, 0.65), makeVect(0.75, 0.65)),
                                       makeSegment(makeVect(0.75, 0.65), makeVect(1, 0.35)),
                                       makeSegment(makeVect(0.75, 0), makeVect(0.6, 0.45)),
                                       makeSegment(makeVect(0.6, 0.45), makeVect(1, 0.15)),
                                       makeSegment(makeVect(0.39, 0.9), makeVect(0.41, 0.9)), # eye
                                       makeSegment(makeVect(0.37, 0.75), makeVect(0.45, 0.8)))) # smile

painterWave(makeFrame(makeVect(0, 0), makeVect(500, 0), makeVect(0, 500)))

im1 = ImageOps.flip(im1)
im1.save("Exercise-2.52-a.jpg", "JPEG")
im1.show()

# Painter transformation & combination
def transformPainter(painter, origin, corner1, corner2):
    def newPainter(frame):
        m = frameCoordMap(frame)
        newOrigin = (lambda f, x: f(x))(m, origin)
        painter(makeFrame(newOrigin, subVect(m(corner1), newOrigin), subVect(m(corner2), newOrigin)))
    return newPainter

def flipVert(painter):
    return transformPainter(painter, makeVect(0, 1), makeVect(1, 1), makeVect(0, 0))

def flipHoriz(painter):
    return transformPainter(painter, makeVect(1, 0), makeVect(0, 0), makeVect(1, 1))

def rotate180(painter):
    return transformPainter(painter, makeVect(1, 1), makeVect(0, 1), makeVect(1, 0))

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

def rightSplit(painter, n):
    if n == 0:
        return painter
    else:
        smaller = rightSplit(painter, n - 1)
        return beside(painter, below(smaller, smaller))

def upSplit(painter, n):
    if n == 0:
        return painter
    else:
        smaller = upSplit(painter, n - 1)
        return below(painter, beside(smaller, smaller))

def cornerSplit(painter, n):
    if n == 0:
        return painter
    else:
        up = upSplit(painter, n - 1)
        right = rightSplit(painter, n - 1)
        corner = cornerSplit(painter, n - 1)
        return beside(below(painter, up), below(right, corner))

im2 = Image.new("RGB", IMAGE_SIZE, "white")
draw = ImageDraw.Draw(im2)

painter = cornerSplit(painterWave, 4)
painter(makeFrame(makeVect(0, 0), makeVect(500, 0), makeVect(0, 500)))

im2 = ImageOps.flip(im2)
im2.save("Exercise-2.52-b.jpg", "JPEG")
im2.show()

# High-order painter operations
def squareOfFour(tl, tr, bl, br):
    def painterPattern(painter):
        top = beside(tl(painter), tr(painter))
        bottom = beside(bl(painter), br(painter))
        return below(bottom, top)
    return painterPattern

def squareLimit(painter, n):
    combine4 = squareOfFour(flipHoriz, lambda painter: painter, rotate180, flipVert)
    return combine4(rotate180(cornerSplit(painter, n)))

im3 = Image.new("RGB", IMAGE_SIZE, "white")
draw = ImageDraw.Draw(im3)

painter = squareLimit(painterWave, 4)
painter(makeFrame(makeVect(0, 0), makeVect(500, 0), makeVect(0, 500)))

im3 = ImageOps.flip(im3)
im3.save("Exercise-2.52-c.jpg", "JPEG")
im3.show()

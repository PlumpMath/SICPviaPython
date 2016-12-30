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

# primitive picture language procedures
from PIL import Image, ImageDraw, ImageOps
IMAGE_SIZE = (500, 500)
im = Image.new("RGB", IMAGE_SIZE, "white")
draw = ImageDraw.Draw(im)

def drawLine(vect1, vect2):
    draw.line([(xcorVect(vect1), ycorVect(vect1)), (xcorVect(vect2), ycorVect(vect2))], fill = 0)

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
def makeSegment(start, end):
    return cons(start, end)

def startSegment(segment):
    return car(segment)

def endSegment(segment):
    return cdr(segment)

def segmentsPainter(segmentList):
    return lambda frame: forEach(lambda segment: drawLine((lambda f, x: f(x))(frameCoordMap(frame), startSegment(segment)),
                                                          (lambda f, x: f(x))(frameCoordMap(frame), endSegment(segment))),
                                 segmentList)

painterA = segmentsPainter(makeList(makeSegment(makeVect(0, 0), makeVect(0, 1)),
                                    makeSegment(makeVect(0, 1), makeVect(1, 1)),
                                    makeSegment(makeVect(1, 1), makeVect(1, 0)),
                                    makeSegment(makeVect(1, 0), makeVect(0, 0))))

painterB = segmentsPainter(makeList(makeSegment(makeVect(0, 0), makeVect(1, 1)),
                                    makeSegment(makeVect(0, 1), makeVect(1, 0))))

painterC = segmentsPainter(makeList(makeSegment(makeVect(0, 0.5), makeVect(0.5, 1)),
                                    makeSegment(makeVect(0.5, 1), makeVect(1, 0.5)),
                                    makeSegment(makeVect(1, 0.5), makeVect(0.5, 0)),
                                    makeSegment(makeVect(0.5, 0), makeVect(0, 0.5))))

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
                                       makeSegment(makeVect(0.6, 0.45), makeVect(1, 0.15))))

painterWave(makeFrame(makeVect(0, 0), makeVect(500, 0), makeVect(0, 500)))

im = ImageOps.flip(im)
im.save("Exercise-2.49.jpg", "JPEG")
im.show()

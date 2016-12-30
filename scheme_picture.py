from scheme_primitive import *

# 2.2
def make_vect(xcor, ycor):
    return cons(xcor, ycor)

def xcor_vect(vect):
    return car(vect)

def ycor_vect(vect):
    return cdr(vect)

def add_vect(vect1, vect2):
    return make_vect(xcor_vect(vect1) + xcor_vect(vect2), ycor_vect(vect1) + ycor_vect(vect2))

def sub_vect(vect1, vect2):
    return make_vect(xcor_vect(vect1) - xcor_vect(vect2), ycor_vect(vect1) - ycor_vect(vect2))

def scale_vect(s, vect):
    return make_vect(s * xcor_vect(vect), s * ycor_vect(vect))

def make_frame(origin, edge1, edge2):
    return cons(origin, cons(edge1, edge2))

def origin_frame(frame):
    return car(frame)

def edge1_frame(frame):
    return car(cdr(frame))

def edge2_frame(frame):
    return cdr(cdr(frame))

def frame_coord_map(frame):
    return lambda v: add_vect(origin_frame(frame),
                              add_vect(scale_vect(xcor_vect(v), edge1_frame(frame)),
                                       scale_vect(ycor_vect(v), edge2_frame(frame))))

def transform_painter(painter, origin, corner1, corner2):
    def new_painter(frame):
        m = frame_coord_map(frame)
        new_origin = m(origin)
        painter(make_frame(new_origin, sub_vect(m(corner1), new_origin), sub_vect(m(corner2), new_origin)))
    return new_painter

from PIL import Image, ImageDraw, ImageOps

def new_picture(width, height):
    global IMAGE_SIZE, IM
    IMAGE_SIZE = (width, height)
    IM = Image.new("RGB", IMAGE_SIZE, "white")

def rogers(frame):
    global IMAGE_SIZE, IM
    rogers_original = ImageOps.flip(Image.open("rogers.gif"))
    w, h = rogers_original.size
    a = xcor_vect(origin_frame(frame))
    b = ycor_vect(origin_frame(frame))
    c = xcor_vect(edge1_frame(frame))
    d = ycor_vect(edge1_frame(frame))
    e = xcor_vect(edge2_frame(frame))
    f = ycor_vect(edge2_frame(frame))
    m = w / (c * f - d * e)
    n = h / (d * e - c * f)
    transformed = rogers_original.transform(IMAGE_SIZE, Image.AFFINE, (f * m, - e * m, (b * e - a * f) * m, d * n, - c * n, (b * c - a * d) * n))
    mask = Image.new('1', IMAGE_SIZE)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.polygon([(a, b), (a + c, b + d), (a + c + e, b + d + f), (a + e, b + f)], fill = 255)
    IM.paste(transformed, (0, 0), mask = mask)

def save_picture(filename):
    global IM
    IM = ImageOps.flip(IM)
    IM.save(filename, "JPEG")
    IM.show()

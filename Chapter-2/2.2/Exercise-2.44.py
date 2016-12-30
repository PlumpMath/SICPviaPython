from scheme_picture import *

def beside(painter1, painter2):
    split_point = make_vect(0.5, 0)
    paint_left = transform_painter(painter1, make_vect(0, 0), split_point, make_vect(0, 1))
    paint_right = transform_painter(painter2, split_point, make_vect(1, 0), make_vect(0.5, 1))
    def new_painter(frame):
        paint_left(frame)
        paint_right(frame)
    return new_painter 

def below(painter1, painter2):
    split_point = make_vect(0, 0.5)
    paint_up = transform_painter(painter1, make_vect(0, 0), make_vect(1, 0), split_point)
    paint_down = transform_painter(painter2, split_point, make_vect(1, 0.5), make_vect(0, 1))
    def new_painter(frame):
        paint_up(frame)
        paint_down(frame)
    return new_painter

def right_split(painter, n):
    if n == 0:
        return painter
    else:
        smaller = right_split(painter, n - 1)
        return beside(painter, below(smaller, smaller))

def up_split(painter, n):
    if n == 0:
        return painter
    else:
        smaller = up_split(painter, n - 1)
        return below(painter, beside(smaller, smaller))

def corner_split(painter, n):
    if n == 0:
        return painter
    else:
        up = up_split(painter, n - 1)
        right = right_split(painter, n - 1)
        top_left = beside(up, up)
        bottom_right = below(right, right)
        corner = corner_split(painter, n - 1)
        return beside(below(painter, top_left), below(bottom_right, corner))

new_picture(500, 500)
corner_split(rogers, 4)(make_frame(make_vect(0, 0), make_vect(500, 0), make_vect(0, 500)))
save_picture("Exercise-2.44.jpg")

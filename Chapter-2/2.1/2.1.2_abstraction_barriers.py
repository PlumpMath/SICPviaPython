from scheme_primitive import *

# Exercise-2.2
# Point constructor & selectors
def make_point(x, y):
    return cons(x, y)

def x_point(point):
    return car(point)

def y_point(point):
    return cdr(point)

# Point display
def print_point(p):
    print("(" + str(x_point(p)) + ", " + str(y_point(p)) + ")")

# Segment constructor & selectors
def make_segment(start_point, end_point):
    return cons(start_point, end_point)

def start_segment(segment):
    return car(segment)

def end_segment(segment):
    return cdr(segment)

def midpoint_segment(segment):
    return make_point((x_point(start_segment(segment)) + x_point(end_segment(segment))) / 2,
                      (y_point(start_segment(segment)) + y_point(end_segment(segment))) / 2)

# Exercise-2.3
# Rectangle constructor & selectors 1
def make_rect(lower_left_point, upper_right_point):
    return cons(lower_left_point, upper_right_point)

def width_rect(rect):
    return abs(x_point(cdr(rect)) - x_point(car(rect)))

def height_rect(rect):
    return abs(y_point(cdr(rect)) - y_point(cdr(rect)))

# Rectangle constructor & selectors 2
def make_rect(point, width, height):
    return cons(point, cons(width, height))

def width_rect(rect):
    return car(cdr(rect))

def height_rect(rect):
    return cdr(cdr(rect))

# Perimeter & area
def perimeter_rect(rect):
    return 2 * (width_rect(rect) + height_rect(rect))

def area_rect(rect):
    return width_rect(rect) * height_rect(rect)

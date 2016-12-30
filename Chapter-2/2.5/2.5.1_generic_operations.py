from scheme_primitive import *
from fractions import gcd
from math import sqrt, atan, sin, cos

# Exercise 2.78
def attach_tag(type_tag, contents):
    if is_number(contents):
        return contents
    else:
        return cons(type_tag, contents)

def type_tag(datum):
    if is_number(datum):
        return "scheme_number"
    elif is_pair(datum):
        return car(datum)
    else:
        raise Exception("Bad tagged datum -- TYPE-TAG")

def contents(datum):
    if is_number(datum):
        return datum
    elif is_pair(datum):
        return cdr(datum)
    else:
        raise Exception("Bad tagged datum -- CONTENTS")

def apply_generic(op, *args):
    type_tags = scm_map(type_tag, scm_list(*args))
    proc = get(op, type_tags)
    if proc:
        return apply(proc, scm_map(contents, args))
    else:
        raise Exception("No method for these types -- APPLY-GENERIC")

# generic arithmetic procedures
def add(x, y):
    return apply_generic("add", x, y)

def sub(x, y):
    return apply_generic("sub", x, y)

def mul(x, y):
    return apply_generic("mul", x, y)

def div(x, y):
    return apply_generic("div", x, y)]

def is_equ(x, y):    # Exercise 2.79
    return apply_generic("is_equ", x, y)

def is_zero(x):    # Exercise 2.80
    return apply_generic("is_zero", x)

# ordinary number package
def install_scheme_number_package():
    def tag(x):
        return attach_tag("scheme_number", x)
    put("add", scm_list("scheme_number", "scheme_number"), lambda x, y: tag(x + y))
    put("sub", scm_list("scheme_number", "scheme_number"), lambda x, y: tag(x - y))
    put("mul", scm_list("scheme_number", "scheme_number"), lambda x, y: tag(x * y))
    put("div", scm_list("scheme_number", "scheme_number"), lambda x, y: tag(x / y))
    put("is_equ", scm_list("scheme_number", "scheme_number"), lambda x, y: x == y)    # Exercise 2.79
    put("is_zero", scm_list("scheme_number"), lambda x: x == 0)    # Exercise 2.80
    put("make", "scheme_number", lambda x: tag(x))
    print("done")

def make_scheme_number(n):
    return get("make", "scheme_number")(n)

# rational package
def install_rational_package():
    # internal procedures
    def numer(x):
        return car(x)
    def denom(x):
        return cdr(x)
    def make_rat(n, d):
        g = gcd(n, d)
        return cons(n // g, d // g)
    def add_rat(x, y):
        return make_rat(numer(x) * denom(y) + numer(y) * denom(x), denom(x) * denom(y))
    def sub_rat(x, y):
        return make_rat(numer(x) * denom(y) - numer(y) * denom(x), denom(x) * denom(y))
    def mul_rat(x, y):
        return make_rat(numer(x) * numer(y), denom(x) * denom(y))
    def div_rat(x, y):
        return make_rat(numer(x) * denom(y), denom(x) * numer(y))
    # interface to rest of the system
    def tag(x):
        return attach_tag("rational", x)
    put("add", scm_list("rational", "rational"), lambda x, y: tag(add_rat(x, y)))
    put("sub", scm_list("rational", "rational"), lambda x, y: tag(sub_rat(x, y)))
    put("mul", scm_list("rational", "rational"), lambda x, y: tag(mul_rat(x, y)))
    put("div", scm_list("rational", "rational"), lambda x, y: tag(div_rat(x, y)))
    put("is_equ", scm_list("rational", "rational"), lambda x, y: numer(x) == numer(y) and denom(x) == denom(y))    # Exercise 2.79
    put("is_zero", scm_list("rational"), lambda x: numer(x) == 0)    # Exercise 2.80
    put("make", "rational", lambda n, d: tag(make_rat(n, d)))
    print("done")

def make_rational(n, d):    
    return get("make", "rational")(n, d)

# rectangular package
def install_rectangular_package():
    # internal procedures
    def real_part(z):
        return car(z)
    def imag_part(z):
        return cdr(z)
    def make_from_real_imag(x, y):
        return cons(x, y)
    def magnitude(z):
        return sqrt(real_part(z) ** 2 + imag_part(z) ** 2)
    def angle(z):
        return atan(imag_part(z) / real_part(z))
    def make_from_mag_ang(r, a):
        return cons(r * cos(a), r * sin(a))
    # interface to the rest of the system
    def tag(x):
        return attach-tag("rectangular", x)
    put("real_part", scm_list("rectangular"), real_part)
    put("imag_part", scm_list("rectangular"), imag_part)
    put("magnitude", scm_list("rectangular"), magnitude)
    put("angle", scm_list("rectangular"), angle)
    put("make_from_real_imag", "rectangular", lambda x, y: tag(make_from_real_imag(x, y)))
    put("make_from_mag_ang", "rectangular", lambda r, a: tag(make_from_mag_ang(r, a)))
    print("done")

# polar package
def install_polar_package():
    # internal procedures
    def magnitude(z):
        return car(z)
    def angle(z):
        return cdr(z)
    def make_from_mag_ang(r, a):
        return cons(r, a)
    def real_part(z):
        return magnitude(z) * cos(angle(z))
    def imag_part(z):
        return magnitude(z) * sin(angle(z))
    def make_from_real_imag(x, y):
        return cons(sqrt(x ** 2 + y ** 2), atan(y / x))
    # interface to the rest of the system
    def tag(x):
        return attach-tag("polar", x)
    put("real_part", scm_list("polar"), real_part)
    put("imag_part", scm_list("polar"), imag_part)
    put("magnitude", scm_list("polar"), magnitude)
    put("angle", scm_list("polar"), angle)
    put("make_from_real_imag", "polar", lambda x, y: tag(make_from_real_imag(x, y)))
    put("make_from_mag_ang", "polar", lambda r, a: tag(make_from_mag_ang(r, a)))
    print("done")

def real_part(z):
    return apply_generic("real_part", z)

def imag_part(z):
    return apply_generic("imag_part", z)

def magnitude(z):
    return apply_generic("magnitude", z)

def angle(z):
    return apply_generic("angle", z)

# complex package
def install_complex_package():
    # imported procedures from rectangular and polar packages
    def make_from_real_imag(x, y):
        return get("make_from_real_imag", "rectangular")(x, y)
    def make_from_mag_ang(r, a):
        return get("make_from_mag_ang", "polar")(r, a)
    # internal procedures
    def add_complex(z1, z2):
        return make_from_real_image(real_part(z1) + real_part(z2), imag_part(z1) + imag_part(z2))
    def sub_complex(z1, z2):
        return make_from_real_image(real_part(z1) - real_part(z2), imag_part(z1) - imag_part(z2))
    def mul_complex(z1, z2):
        return make_from_mag_ang(magnitude(z1) * magnitude(z2), angle(z1) + angle(z2))
    def div_complex(z1, z2):
        return make_from_mag_ang(magnitude(z1) / magnitude(z2), angle(z1) - angle(z2))
    # interface to rest of the system
    def tag(z):
        return attach_tag("complex", z)
    put("add", scm_list("complex", "complex"), lambda z1, z2: tag(add_complex(z1, z2)))
    put("sub", scm_list("complex", "complex"), lambda z1, z2: tag(sub_complex(z1, z2)))
    put("mul", scm_list("complex", "complex"), lambda z1, z2: tag(mul_complex(z1, z2)))
    put("div", scm_list("complex", "complex"), lambda z1, z2: tag(div_complex(z1, z2)))
    put("is_equ", scm_list("complex", "complex"), lambda z1, z2: real_part(z1) == real_part(z2) and imag_part(z1) == imag_part(z2))    # Exercise 2.79
    put("is_zero", scm_list("complex"), lambda x: real_part(x) == 0 and imag_part == 0)    # Exercise 2.80
    put("real_part", scm_list("complex"), real_part)    # Exercise 2.77
    put("imag_part", scm_list("complex"), imag_part)    # Exercise 2.77
    put("magnitude", scm_list("complex"), magnitude)    # Exercise 2.77
    put("angle", scm_list("complex"), angle)
    put("make_from_real_imag", "complex", lambda x, y: tag(make_from_real_imag(x, y)))
    put("make_from_man_ang", "complex", lambda r, a: tag(make_from_man_ang(r, a)))
    print("done")

def make_complex_from_real_image(x, y):
    return get("make_from_real_imag", "complex")(x, y)

def make_complex_from_mag_ang(r, a):
    return get("make_from_mag_ang", "complex")(r, a)

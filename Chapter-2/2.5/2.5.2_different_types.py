from scheme_primitive import *
from fractions import gcd
from math import sqrt, atan, sin, cos

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

# Exercise 2.81
def apply_generic(op, *args):
    type_tags = scm_map(type_tag, scm_list(*args))
    proc = get(op, type_tags)
    def no_method():
        raise Exception("No method for these types -- APPLY-GENERIC")
    if proc:
        return apply(proc, scm_map(contents, scm_list(*args)))
    elif length(scm_list(*args)) == 2:
        type1 = car(type_tags)
        type2 = cadr(type_tags)
        a1 = car(scm_list(*args))
        a2 = cadr(scm_list(*args))
        if type1 == type2:
            no_method()
        else:
            t1_to_t2 = get_coercion(type1, type2)
            t2_to_t1 = get_coercion(type2, type1)
            if t1_to_t2:
                return apply_generic(op, t1_to_t2(a1), a2)
            elif t2_to_t1:
                return apply_generic(op, a1, t2_to_t1(a2))
            else:
                no_method()
    else:
        no_method()

# Exercise 2.82
def apply_generic(op, *args):
    type_tags = scm_map(type_tag, scm_list(*args))
    proc = get(op, type_tags)
    def find_target(types):
        def can_coerce(types, target):
            if types == None:
                return True
            else:
                first = car(types)
                if first == target or get_coercion(first, target):
                    return can_coerce(cdr(types), target)
                else:
                    return False
        if types == None:
            return False
        else:
            first = car(types)
            if can_coerce(types, first):
                return first
            else:
                return find_target(cdr(types))
    def all_coerce_to(items, target):
        if items == None:
            return None
        else:
            first = car(items)
            return cons(get_coercion(type_tag(first), target)(first), all_coerce_to(cdr(items), target))
    if proc:
        return apply(proc, scm_list(contents, scm_list(*args)))
    else:
        target_type = find_target(type_tags)
        coerced_args = all_coerce_to(scm_list(*args), target_type)
        coerced_types = scm_map(type_tag, coerced_types)
        coerced_proc = get(op, coerced_types)
        if coerced_proc:
            return apply(apply_generic, append(scm_list(op), coerced_args))
        else:
            raise Exception("No method for these types -- APPLY-GENERIC")

# Exercise 2.84
type_tower = scm_list("integer", "rational", "real", "complex")

def apply_generic(op, *args):
    type_tags = scm_map(type_tag, scm_list(*args))
    proc = get(op, type_tags)
    def find_target(tower, types):
        def filter_type(target, types):
            if types == None:
                return None
            elif car(types) == target:
                return filter_type(target, cdr(f))
            else:
                return cons(car(f), filter_type(target, cdr(f)))
        def iter_find_target(highest, remaining_tower, remaining_types):
            if remaining_types == None:
                return highest
            elif remaining_tower == None:
                raise Exception("Can't find highest type")
            else:
                new_highest = car(remaining_tower)
                return iter_find_target(new_highest, cdr(remaining_tower), filter_type(new_highest, remaining_types))
        return iter_find_target(None, tower, types)
    def all_raise_to(items, target):
        def raise_to(item, target):
            if type_tag(item) == target:
                return item
            else:
                return raise_to(raise_type(item), target)
        if items == None:
            return None
        else:
            return cons(raise_to(car(items), target), all_raise_to(cdr(items), target))
    if proc:
        return apply(proc, scm_list(contents, scm_list(*args)))
    else:
        target_type = find_target(type_tower, type_tags)
        raised_args = all_raise_to(scm_list(*args), target_type)
        raised_types = scm_map(type_tag, raised_args)
        raised_proc = get(op, raised_types)
        if target_type:
            return drop(apply(apply_generic, append(scm_list(op), raised_args)))    # Exercise 2.85
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

def is_equ(x, y):
    return apply_generic("is_equ", x, y)

def is_zero(x):
    return apply_generic("is_zero", x)

# Exercise 2.81
def exp(x, y):
    return apply_generic("exp", x, y)

# Exercise 2.83
def raise_type(x):
    return apply_generic("raise", x)

# Exercise 2.85
def project(x):
    return apply_generic("project", x)

def drop(x):    # Exercise 2.85
    def simplify(higher, lower):
        raised = raise_type(lower)
        if type_tag(raised) == type_tag(higher) and is_equ(higher, lower):
            return simplify(lower, project(lower))
        else:
            return higher
    return simplify(x, project(x))

# Exercise 2.86
def sine(x):    
    return apply_generic("sine", x)

def cosine(x):
    return apply_generic("cosine", x)

def arctan(x):
    return apply_generic("arctan", x)

def square(x):
    return apply_generic("square", x)

def square_root(x):
    return apply_generic("square_root", x)

# ordinary number package
def install_scheme_number_package():
    def tag(x):
        return attach_tag("scheme_number", x)
    put("add", scm_list("scheme_number", "scheme_number"), lambda x, y: tag(x + y))
    put("sub", scm_list("scheme_number", "scheme_number"), lambda x, y: tag(x - y))
    put("mul", scm_list("scheme_number", "scheme_number"), lambda x, y: tag(x * y))
    put("div", scm_list("scheme_number", "scheme_number"), lambda x, y: tag(x / y))
    put("exp", scm_list("scheme_number", "scheme_number"), lambda x, y: tag(x ** y))    # Exercise 2.81
    put("sine", scm_list("scheme_number"), lambda x: tag(sin(x)))    # Exercise 2.86
    put("cosine", scm_list("scheme_number"), lambda x: tag(cos(x)))    # Exercise 2.86
    put("arctan", scm_list("scheme_number"), lambda x: tag(atan(x)))    # Exercise 2.86
    put("square", scm_list("scheme_number"), lambda x: tag(x ** 2))    # Exercise 2.86
    put("square_root", scm_list("scheme_number"), lambda x: tag(sqrt(x)))    # Exercise 2.86
    put("is_equ", scm_list("scheme_number", "scheme_number"), lambda x, y: x == y)
    put("is_zero", scm_list("scheme_number"), lambda x: x == 0)
    put("make", "scheme_number", lambda x: tag(x))
    print("done")

def make_scheme_number(n):
    return get("make", "scheme_number")(n)

# integer package
def install_integer_package():
    def tag(x):
        return attach_tag("integer", x)
    put("add", scm_list("integer", "integer"), lambda x, y: tag(x + y))
    put("sub", scm_list("integer", "integer"), lambda x, y: tag(x - y))
    put("mul", scm_list("integer", "integer"), lambda x, y: tag(x * y))
    put("div", scm_list("integer", "integer"), lambda x, y: make_rational(x, y))
    put("is_equ", scm_list("integer", "integer"), lambda x, y: x == y)
    put("is_zero", scm_list("integer"), lambda x: x == 0)
    put("make", "integer", lambda x: tag(x))
    put("raise", scm_list("integer"), lambda x: make_rational(n, 1))    # Exercise 2.83
    print("done")

def make_integer(n):    
    return get("make", "integer")(n)

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
    put("sine", scm_list("rational"), lambda x: make_scheme_number(sin(numer(x) / denom(x))))    # Exercise 2.86
    put("cosine", scm_list("rational"), lambda x: make_scheme_number(cos(numer(x) / denom(x))))    # Exercise 2.86
    put("arctan", scm_list("rational"), lambda x: make_scheme_number(atan(numer(x) / denom(x))))    # Exercise 2.86
    put("square", scm_list("rational"), lambda x: tag(mul_rat(x, x)))    # Exercise 2.86
    put("square_root", scm_list("rational"), lambda x: make_scheme_number(sqrt(numer(x) / denom(x))))    # Exercise 2.86
    put("is_equ", scm_list("rational", "rational"), lambda x, y: numer(x) == numer(y) and denom(x) == denom(y))
    put("is_zero", scm_list("rational"), lambda x: numer(x) == 0)
    put("make", "rational", lambda n, d: tag(make_rat(n, d)))
    put("raise", scm_list("rational"), lambda x: make_real(numer(x) / denom(x)))    # Exercise 2.83
    put("project", scm_list("rational"), lambda x: make_integer(numer(x) // denom(x))    # Exercise 2.85
    print("done")

def make_rational(n, d):    
    return get("make", "rational")(n, d)

# real package
def install_real_package():
    def tag(x):
        return attach_tag("real", x)
    put("add", scm_list("real", "real"), lambda x, y: tag(x + y))
    put("sub", scm_list("real", "real"), lambda x, y: tag(x - y))
    put("mul", scm_list("real", "real"), lambda x, y: tag(x * y))
    put("div", scm_list("real", "real"), lambda x, y: tag(x / y))
    put("is_equ", scm_list("real", "real"), lambda x, y: x == y)
    put("is_zero", scm_list("real"), lambda x: x == 0)
    put("make", "real", lambda x: tag(x))
    put("raise", scm_list("real"), lambda x: make_complex_from_real_image(x, 0))    # Exercise 2.83
    put("project", scm_list("real"), lambda x: make_integer(int(round(x)))    # Exercise 2.85
    print("done")

def make_real(x):
    return get("make", "real")(x)

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
        return square_root(add(square(real_part(z)), square(imag_part(z))))    # Exercise 2.86
    def angle(z):
        return arctan(div(imag_part(z), real_part(z)))    # Exercise 2.86
    # def make_from_mag_ang(r, a):
    #    return cons(r * cos(a), r * sin(a))
    # interface to the rest of the system
    def tag(x):
        return attach-tag("rectangular", x)
    put("real_part", scm_list("rectangular"), real_part)
    put("imag_part", scm_list("rectangular"), imag_part)
    put("magnitude", scm_list("rectangular"), magnitude)
    put("angle", scm_list("rectangular"), angle)
    put("make_from_real_imag", "rectangular", lambda x, y: tag(make_from_real_imag(x, y)))
    # put("make_from_mag_ang", "rectangular", lambda r, a: tag(make_from_mag_ang(r, a)))
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
        return mul(magnitude(z), cosine(angle(z)))    # Exercise 2.86
    def imag_part(z):
        return mul(magnitude(z), sine(angle(z)))    # Exercise 2.86
    # def make_from_real_imag(x, y):
    #    return cons(sqrt(x ** 2 + y ** 2), atan(y / x))
    # interface to the rest of the system
    def tag(x):
        return attach-tag("polar", x)
    put("real_part", scm_list("polar"), real_part)
    put("imag_part", scm_list("polar"), imag_part)
    put("magnitude", scm_list("polar"), magnitude)
    put("angle", scm_list("polar"), angle)
    # put("make_from_real_imag", "polar", lambda x, y: tag(make_from_real_imag(x, y)))
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
        return make_from_real_image(add(real_part(z1), real_part(z2)), add(imag_part(z1), imag_part(z2)))    # Exercise 2.86
    def sub_complex(z1, z2):
        return make_from_real_image(sub(real_part(z1), real_part(z2)), sub(imag_part(z1), imag_part(z2)))    # Exercise 2.86
    def mul_complex(z1, z2):
        return make_from_mag_ang(mul(magnitude(z1), magnitude(z2)), add(angle(z1), angle(z2)))    # Exercise 2.86
    def div_complex(z1, z2):
        return make_from_mag_ang(div(magnitude(z1), magnitude(z2)), sub(angle(z1), angle(z2)))    # Exercise 2.86
    # interface to rest of the system
    def tag(z):
        return attach_tag("complex", z)
    put("add", scm_list("complex", "complex"), lambda z1, z2: tag(add_complex(z1, z2)))
    put("sub", scm_list("complex", "complex"), lambda z1, z2: tag(sub_complex(z1, z2)))
    put("mul", scm_list("complex", "complex"), lambda z1, z2: tag(mul_complex(z1, z2)))
    put("div", scm_list("complex", "complex"), lambda z1, z2: tag(div_complex(z1, z2)))
    put("is_equ", scm_list("complex", "complex"), lambda z1, z2: real_part(z1) == real_part(z2) and imag_part(z1) == imag_part(z2))
    put("real_part", scm_list("complex"), real_part)
    put("imag_part", scm_list("complex"), imag_part)
    put("magnitude", scm_list("complex"), magnitude)
    put("angle", scm_list("complex"), angle)
    put("is_zero", scm_list("complex"), lambda x: real_part(x) == 0 and imag_part == 0)
    put("make_from_real_imag", "complex", lambda x, y: tag(make_from_real_imag(x, y)))
    put("make_from_man_ang", "complex", lambda r, a: tag(make_from_man_ang(r, a)))
    put("project", scm_list("complex"), lambda x: make_real(real_part(x)))    # Exercise 2.85
    print("done")

def make_complex_from_real_image(x, y):
    return get("make_from_real_imag", "complex")(x, y)

def make_complex_from_mag_ang(r, a):
    return get("make_from_mag_ang", "complex")(r, a)

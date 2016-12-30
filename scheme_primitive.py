# print
def scm_print(items):
    def display_item(x):
        if x == None:
            return "()"
        elif not callable(x):
            return str(x)
        else:
            return "({0})".format(display_pair(x))
    def display_pair(x):
        if cdr(x) == None:
            return display_item(car(x))
        elif not callable(cdr(x)):
            return display_item(car(x)) + ", " + display_item(cdr(x))
        else:
            return display_item(car(x)) + ", " + display_pair(cdr(x))
    print(display_item(items))

# 2.1
def cons(x, y):
    def set_x(v):
        nonlocal x
        x = v
    def set_y(v):
        nonlocal y
        y = v
    def dispatch(m):
        if m == "car":
            return x
        elif m == "cdr":
            return y
        elif m == "set_car":
            return set_x
        elif m == "set_cdr":
            return set_y
        else:
            raise Exception("Undefined operation -- CONS")
    return dispatch

def car(z):
    return z("car")

def cdr(z):
    return z("cdr")

def set_car(z, new_value):
    z("set_car")(new_value)

def set_cdr(z, new_value):
    z("set_cdr")(new_value)

def cadr(x):
    return car(cdr(x))

def cddr(x):
    return cdr(cdr(x))

# 2.2
def scm_list(*items):
    if items == ():
        return None
    else:
        return cons(items[0], scm_list(*items[1:]))

def scm_map(proc, *seqs):
    if None in seqs:
        return None
    else:
        return cons(proc(*map(car, seqs)), scm_map(proc, *map(cdr, seqs)))

def is_pair(x):
    return callable(x)

def accumulate(op, initial, sequence):
    if sequence == None:
        return initial
    else:
        return op(car(sequence), accumulate(op, initial, cdr(sequence)))

def append(seq1, seq2):
    return accumulate(cons, seq2, seq1)

def length(sequence):
    return accumulate(lambda x, y: 1 + y, 0, sequence)

def accumulate_n(op, init, seqs):
    if car(seqs) == None:
        return None
    else:
        return cons(accumulate(op, init, scm_map(car, seqs)),
                    accumulate_n(op, init, scm_map(cdr, seqs)))

# 2.3
def memq(item, x):
    if x == None:
        return False
    elif item == car(x):
        return x
    else:
        return memq(item, cdr(x))

def is_symbol(x):
    return type(x) == str

def is_number(x):
    from numbers import Number
    return isinstance(x, Number)

# 2.4
def put(op, typ, item):
    pass

def get(op, typ):
    pass

def apply(proc, seq):
    def list_to_tuple(s):
        if s == None:
            return ()
        else:
            return (car(s),) + list_to_tuple(cdr(s))
    return proc(*list_to_tuple(seq))

def put_coercion(type1, type2, op):
    pass

def get_coercion(type1, type2):
    pass

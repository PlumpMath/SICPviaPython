from scheme_primitive import *

# Exercise 2.73
def deriv(exp, var):
    if is_number(exp):
        return 0
    elif is_symbol(exp):
        if exp == var:
            return 1
        else:
            return 0
    else:
        return get("deriv", operator(exp))(operands(exp), var)

def operator(exp):
    return car(exp)

def operands(exp):
    return cdr(exp)

# Package
def install_deriv_package():
    # sum
    def addend(oprd):
        return car(oprd)
    def augend(s):
        return cadr(oprd)
    def make_sum(x, y):
        if is_number(x) and x == 0:
            return y
        elif is_number(y) and y == 0:
            return x
        elif is_number(x) and is_number(y):
            return x + y
        else:
            return scm_list("+", x, y)
    def sum_deriv(oprd, var):
        return make_sum(deriv(addend(oprd), var), deriv(augend(oprd), var))
    # product
    def multiplier(oprd):
        return car(oprd)
    def multiplicand(oprd):
        return cadr(oprd)
    def make_product(x, y):
        if (is_number(x) and x == 0) or (is_number(y) and y == 0):
            return 0
        elif is_number(x) and x == 1:
            return y
        elif is_number(y) and y == 1:
            return x
        elif is_number(x) and is_number(y):
            return x * y
        else:
            return scm_list("*", x, y)
    def product_deriv(oprd, var):
        return make_sum(make_product(multiplier(oprd), deriv(multiplicand(oprd), var)),
                        make_product(deriv(multiplier(oprd), var), multiplicand(oprd)))
    # exponentation
    def base(oprd):
        return car(oprd)
    def exponent(oprd):
        return cadr(oprd)
    def make_exponentation(x, n):
        if is_number(n) and n == 0:
            return 1
        elif is_number(n) and n == 1:
            return x
        elif is_number(n) and is_number(x):
            return x ** n
        else:
            return makeList("**", x, n)
    def exponentation_deriv(oprd, var):
        return make_product(make_product(exponent(oprd), make_exponentation(base(oprd), make_sum(exponent(oprd), -1))),
                            deriv(base(oprd), var))
    put("deriv", "+", sum_deriv)
    put("deriv", "*", product_deriv)
    put("deriv", "**", exponentation_deriv)
    # To index the procedures in the opposite way:
    #put("+", "deriv", sum_deriv)
    #put("*", "deriv", product_deriv)
    #put("**", "deriv", exponentation_deriv)
    print("done")

# Exercise 2.74
# a
def get_record(division, employee_name):
    return get(division, "record")(employee_name)
# b
def get_salary(division, record):
    return get(division, "salary")(record)
# c
def find_employee_record(employee_name, division_list):
    if division_list == None:
        return False
    employee = get_record(car(division_list), employee_name)
    if employee:
        return employee
    else:
        return find_employee_record(employee_name, cdr(division_list))
# d
# install new "get_record" and "get_salary" procedures

# Exercise 2.75
from math import sin, cos

def make_from_mag_ang(r, a):
    def dispatch(op):
        if op == "magnitude":
            return r
        elif op == "angle":
            return a
        elif op == "real_part":
            return r * cos(a)
        elif op == "imag_part":
            return r * sin(a)
        else:
            raise Exception("Unknow op -- MAKE-FROM-REAL-IMAGE: " + op)
    return dispatch

# Exercise 2.76
# Data-directed style or Message-passing style is the most appropriate when new types must often be added.
# Data-directed style is the most appropriate when new operations must often be added.

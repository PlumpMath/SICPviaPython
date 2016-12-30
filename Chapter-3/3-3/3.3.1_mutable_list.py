from scheme_primitive import *

# Exercise 3.12
def last_pair(x):
    if cdr(x) == None:
        return x
    else:
        return last_pair(cdr(x))

def append_set(x, y):
    set_cdr(last_pair(x), y)
    return x

x = scm_list("a", "b")
y = scm_list("c", "d")
z = append(x, y)

scm_print(z)
# (a, b, c, d)
scm_print(cdr(x))
# (b)

w = append_set(x, y)

scm_print(w)
# (a, b, c, d)
scm_print(x)
# (a, b, c, d)

# Exercise 3.13
def make_cycle(x):
    set_cdr(last_pair(x), x)
    return x

z = make_cycle(scm_list("a", "b", "c"))

scm_print(last_pair(z))
# RecursionError: maximum recursion depth exceeded in comparison

# Exercise 3.14
def mystery(x):
    def loop(x, y):
        if x == None:
            return y
        else:
            temp = cdr(x)
            set_cdr(x, y)
            return loop(temp, x)
    return loop(x, None)

v = scm_list("a", "b", "c", "d")
w = mystery(v)

scm_print(v)
# (a)
scm_print(w)
# (d, c, b, a)

# Exercise 3.15
x = scm_list("a", "b")
z1 = cons(x, x)
z2 = cons(scm_list("a", "b"), scm_list("a", "b"))

def set_to_wow(x):
    set_car(car(x), "wow")
    return x

scm_print(z1)
# ((a, b), a, b)
scm_print(set_to_wow(z1))
# ((wow, b), wow, b)
scm_print(z2)
# ((a, b), a, b)
scm_print(set_to_wow(z2))
# ((wow, b), a, b)

# Exercise 3.15
def count_pairs(x):
    if not is_pair(x):
        return 0
    else:
        return count_pairs(car(x)) + count_pairs(cdr(x)) + 1

first = scm_list("a", "b", "c")
print(count_pairs(first))
# 3
x = scm_list("a")
second = scm_list(x, x)
print(count_pairs(second))
# 4
y = cons(x, x)
third = cons(y, y)
print(count_pairs(third))
# 7
fourth = make_cycle(scm_list("a", "b", "c"))
print(count_pairs(fourth))
#  RecursionError: maximum recursion depth exceeded in comparison

# Exercise 3.17
def count_pairs(x):
    def count_iter(x, cons_list):
        if is_pair(x) and not memq(x, cons_list):
            return count_iter(car(x), count_iter(cdr(x), cons(x, cons_list)))
        else:
            return cons_list
    return length(count_iter(x, None))
print(count_pairs(first))
# 3
print(count_pairs(second))
# 3
print(count_pairs(third))
# 3
print(count_pairs(fourth))
# 3

# Exercise 3.18
def has_cycle(x):
    def cycle_iter(x, cons_list):
        if not is_pair(x):
            return False
        elif memq(x, cons_list):
            return True
        else:
            return cycle_iter(cdr(x), cons(x, cons_list))
    return cycle_iter(x, None)

print(has_cycle(fourth))
# True

# Exercise 3.19
def has_cycle(x):
    def tortoise_and_hare(tortoise, hare):
        if hare == None:
            return False
        elif tortoise == hare:
            return True
        else:
            return tortoise_and_hare(cdr(tortoise), cddr(hare))
    return tortoise_and_hare(x, x)

print(has_cycle(fourth))
# True

# Exercise 3.20
x = cons(1, 2)
z = cons(x, x)
set_car(cdr(z), 17)

print(car(x))
# 17

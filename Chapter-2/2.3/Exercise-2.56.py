# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
cadr = lambda x: car(cdr(x))
caddr = lambda x: car(cdr(cdr(x)))
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

def printList(items):
    displayList = lambda items: '[' + displayItems(items) + ']' 
    displayItems = lambda items: displayItem(car(items)) if cdr(items) == None \
                   else displayItem(car(items)) + ', ' + displayItem(cdr(items)) if not callable(cdr(items)) \
                   else displayItem(car(items)) + ', ' + displayItems(cdr(items))
    displayItem = lambda item: '[]' if item == None \
                  else str(item) if not callable(item) \
                  else displayList(item)
    print(displayList(items))

# Symbolic Differentiation
from numbers import Number
def isNumber(exp):
    return isinstance(exp, Number)

def equalNumber(exp, num):
    return isNumber(exp) and exp == num

def isVariable(x):
    return type(x) == str

def sameVariable(v1, v2):
    return isVariable(v1) and isVariable(v2) and v1 == v2

def makeSum(a1, a2):
    if equalNumber(a1, 0):
        return a2
    elif equalNumber(a2, 0):
        return a1
    elif isNumber(a1) and isNumber(a2):
        return a1 + a2
    else:
        return makeList("+", a1, a2)

def makeProduct(m1, m2):
    if equalNumber(m1, 0) or equalNumber(m2, 0):
        return 0
    elif equalNumber(m1, 1):
        return m2
    elif equalNumber(m2, 1):
        return m1
    elif isNumber(m1) and isNumber(m2):
        return m1 * m2
    else:
        return makeList("*", m1, m2)

def makeExponentiation(x, n):
    if equalNumber(n, 0):
        return 1
    elif equalNumber(n, 1):
        return x
    elif isNumber(x) and isNumber(n):
        return x ** n
    else:
        return makeList("**", x, n)

def isSum(x):
    return callable(x) and car(x) == "+"

def addend(s):
    return cadr(s)

def augend(s):
    return caddr(s)

def isProduct(x):
    return callable(x) and car(x) == "*"

def multiplier(p):
    return cadr(p)

def multiplicand(p):
    return caddr(p)

def isExponentiation(x):
    return callable(x) and car(x) == "**"

def base(e):
    return cadr(e)

def exponent(e):
    return caddr(e)

def deriv(exp, var):
    if isNumber(exp):
        return 0
    elif isVariable(exp):
        if sameVariable(exp, var):
            return 1
        else:
            return 0
    elif isSum(exp):
        return makeSum(deriv(addend(exp), var), deriv(augend(exp), var))
    elif isProduct(exp):
        return makeSum(makeProduct(multiplier(exp), deriv(multiplicand(exp), var)),
                       makeProduct(deriv(multiplier(exp), var), multiplicand(exp)))
    elif isExponentiation(exp):
        return makeProduct(makeProduct(exponent(exp), makeExponentiation(base(exp), makeSum(exponent(exp), -1))),
                           deriv(base(exp), var))
    else:
        raise Exception("unknown expression type -- DERIV")

printList(deriv(makeList("+", makeList("+", makeList("*", "a", makeList("**", "x", 2)), makeList("*", "b", "x")), "c"), "x"))
# [+, [*, a, [*, 2, x]], b]

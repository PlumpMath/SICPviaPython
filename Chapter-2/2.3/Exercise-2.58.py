# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
cadr = lambda x: car(cdr(x))
cddr = lambda x: cdr(cdr(x))
caddr = lambda x: car(cdr(cdr(x)))
cdddr = lambda x: cdr(cdr(cdr(x)))
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
memQ = lambda item, x: False if x == None else x if item == car(x) else memQ(item, cdr(x))
appendList = lambda list1, list2: list2 if list1 == None else cons(car(list1), appendList(cdr(list1), list2))

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
        return makeList(a1, "+", a2)

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
        return makeList(m1, "*", m2)

def isSum(x):
    return callable(x) and callable(memQ("+", x))

def addend(s):
    def addendIter(s, result):
        if car(s) == "+":
            return result
        else:
            return addendIter(cdr(s), appendList(result, makeList(car(s))))
    addendList = addendIter(s, None)
    if cdr(addendList) == None:
        return car(addendList)
    else:
        return addendList 

def augend(s):
    augendList = cdr(memQ("+", s))
    if cdr(augendList) == None:
        return car(augendList)
    else:
        return augendList

def isProduct(x):
    return callable(x) and memQ("+", x) == False

def multiplier(p):
    return car(p)

def multiplicand(p):
    if cdddr(p) == None:
        return caddr(p)
    else:
        return cddr(p)

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
    else:
        raise Exception("unknown expression type -- DERIV")

print(deriv(makeList("x", "+", makeList(3, "*", makeList("x", "+", makeList("y", "+", 2)))), "x"))
# 4
print(deriv(makeList("x", "+", 3, "*", makeList("x", "+", "y", "+", 2)), "x"))
# 4

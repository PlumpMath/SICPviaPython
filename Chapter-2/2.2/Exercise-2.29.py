# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

# Binary Mobile
# a.
def makeMobile(left, right):
    return makeList(left, right)

def makeBranch(length, structure):
    return makeList(length, structure)

def leftBranch(mobile):
    return car(mobile)

def rightBranch(mobile):
    return car(cdr(mobile))

def branchLength(branch):
    return car(branch)

def branchStructure(branch):
    return car(cdr(branch))

#b.
def branchWeight(branch):
    if callable(branchStructure(branch)):
        return totalWeight(branchStructure(branch))
    else:
        return branchStructure(branch)

def totalWeight(mobile):
    return branchWeight(leftBranch(mobile)) + \
           branchWeight(rightBranch(mobile))

#c.
def branchTorque(branch):
    return branchLength(branch) * branchWeight(branch)

def branchBalanced(branch):
    if callable(branchStructure(branch)):
        return mobileBalanced(branchStructure(branch))
    else:
        return True

def mobileBalanced(mobile):
    return branchTorque(leftBranch(mobile)) == branchTorque(rightBranch(mobile)) and \
           branchBalanced(leftBranch(mobile)) and \
           branchBalanced(rightBranch(mobile))

#d.
def makeMobile1(left, right):
    return cons(left, right)

def makeBranch1(length, structure):
    return cons(length, structure)

def rightBranch1(branch):
    return cdr(branch)

def branchStructure1(branch):
    return cdr(branch)

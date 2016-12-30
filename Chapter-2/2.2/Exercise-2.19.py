# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

# Change counting
usCoins = makeList(50, 25, 10, 5, 1)
ukCoins = makeList(100, 50, 20, 10, 5, 2, 1, 0.5)

def firstDenomination(coinValues):
    return car(coinValues)

def exceptFirstDenomination(coinValues):
    return cdr(coinValues)

def noMore(coinValues):
    return coinValues == None

def cc(amount, coinValues):
    if amount == 0:
        return 1
    elif amount < 0 or noMore(coinValues):
        return 0
    else:
        return cc(amount, exceptFirstDenomination(coinValues)) + \
               cc(amount - firstDenomination(coinValues), coinValues)

print(cc(100, usCoins))
# 292

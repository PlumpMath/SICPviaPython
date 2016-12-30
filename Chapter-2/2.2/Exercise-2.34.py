# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))
accumulate = lambda op, initial, sequence: initial if sequence == None else op(car(sequence), accumulate(op, initial, cdr(sequence)))

# Horner's rule
def hornerEval(x, coefficientSequence):
    return accumulate(lambda thisCoeff, higherTerm: thisCoeff + 2 * higherTerm, 0, coefficientSequence)

print(hornerEval(2, makeList(1, 3, 0, 5, 0, 1)))
# 79

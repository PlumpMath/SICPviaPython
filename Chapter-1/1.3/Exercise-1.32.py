def accumulateR(combiner, nullValue, term, a, nextOne, b):
    if a > b:
        return nullValue
    else:
        return combiner(term(a), accumulateR(combiner, nullValue, term, nextOne(a), nextOne, b))

def accumulateI(combiner, nullValue, term, a, nextOne, b):
    def accumulateIter(a, result):
        if a > b:
            return result
        else:
            return accumulateIter(nextOne(a), combiner(term(a), result))
    return accumulateIter(a, nullValue)

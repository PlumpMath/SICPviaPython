def add(term, a, nextOne, b):
    def addIter(a, result):
        if a > b:
            return result
        else:
            return addIter(nextOne(a), term(a) + result)
    return addIter(a, 0)

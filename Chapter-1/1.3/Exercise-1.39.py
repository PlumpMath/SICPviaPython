def contFrac(n, d, k):
    def cf(i):
        if i == k:
            return n(i) / d(i)
        else:
            return n(i) / (d(i) + cf(i + 1))
    return cf(1)

def tanCF(x, k):
    return contFrac(lambda i: x if i == 1 else - x ** 2, lambda i: 2 * i - 1, k)

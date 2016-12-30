def fastExpt(b, n):
    def exptIter(result, b, n):
        if n == 0:
            return a
        elif n % 2 == 0:
            return exptIter(a, b * b, n / 2)
        else:
            return exptIter(a * b, b, n - 1)
    print(exptIter(1, b, n))

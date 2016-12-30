# recursive process:
def f1(n):
    if n < 3:
        return n
    else:
        return f1(n - 1) + 2 * f1(n - 2) + 3 * f1(n - 3)

# iterative process:
def f2(n):
    def fIter(a, b, c, count):
        if count == 0:
            return c
        else:
            return fIter(a + 2 * b + 3 * c, a, b, count - 1)
    return fIter(2, 1, 0, n)

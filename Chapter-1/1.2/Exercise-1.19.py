def fib(n):
    def fibIter(a, b, p, q, count):
        if count == 0:
            return b
        elif count % 2 == 0:
            return fibIter(a, b, p ** 2 + q ** 2, q ** 2 + 2 * p * q, count / 2)
        else:
            return fibIter(b * q + a * q + a * p, b * p + a * q, p, q, count - 1)
    print(fibIter(1, 0, 0, 1, n))

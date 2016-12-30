def cont_frac(n, d, k):
    def cf(i):
        if i == k:
            return n(i) / d(i)
        else:
            return n(i) / (d(i) + cf(i + 1))
    return cf(1)

def e(k):
    return cont_frac(lambda i: 1.0, lambda i: 2 * (i + 1) / 3 if i % 3 == 2 else 1.0, k) + 2

print(e(100))
# 2.7182818284590455

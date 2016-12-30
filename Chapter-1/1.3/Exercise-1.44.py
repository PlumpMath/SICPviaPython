DX = 0.00001

def compose(f, g):
    return lambda x: f(g(x))

def repeated(f, n):
    if n == 1:
        return f
    else:
        return compose(f, repeated(f, n - 1))

def smooth(f):
    return lambda x: (f(x - DX) + f(x) + f(x + DX)) / 3

def nFoldSmooth(f, n):
    return (lambda g: g(f))(repeated(smooth, n))

# Scheme primitive procedures
cons = lambda x, y: lambda m: m(x, y)
car = lambda z: z(lambda p, q: p)
cdr = lambda z: z(lambda p, q: q)
makeList = lambda *items: None if items == () else cons(items[0], makeList(*items[1:]))

# Pick 7
print(car(cdr(car(cdr(cdr(makeList(1, 3, makeList(5, 7), 9)))))))
# 7
print(car(car(makeList(makeList(7)))))
# 7
print(car(cdr(car(cdr(car(cdr(car(cdr(car(cdr(car(cdr(makeList(1, makeList(2, makeList(3, makeList(4, makeList(5, makeList(6, 7)))))))))))))))))))
# 7

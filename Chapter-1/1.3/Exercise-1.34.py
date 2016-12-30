def f(g):
  return g(2)

print(f(f))
# TypeError: 'int' object is not callable

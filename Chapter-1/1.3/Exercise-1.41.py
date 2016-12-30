def returnValue(func, x):
    return func(x)

def double(func):
    return lambda x: func(func(x))

inc = lambda x: x + 1

print(returnValue(returnValue(double(double(double)), inc), 5))
# 21

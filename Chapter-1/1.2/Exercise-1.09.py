def add1(a, b):
    if a == 0:
        return b
    else:
        return add1(a - 1, b) + 1
    
print(add1(4, 5))
# 9
# This is recursive

def add2(a, b):
    if a == 0:
        return b
    else:
        return add2((a - 1), (b + 1))

print(add2(4, 5))
# 9
# This is iterative

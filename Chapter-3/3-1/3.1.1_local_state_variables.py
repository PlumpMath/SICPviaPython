# Exercise 3.1
def make_accumulator(x):
    def new_func(y):
        nonlocal x
        x += y
        return x
    return new_func

A = make_accumulator(5)

print(A(10))
# 15
print(A(10))
# 25

# Exercise 3.2
from math import sqrt

def make_monitored(f):
    def mf(x):
        if not hasattr(mf, "counter"):
            mf.counter = 0
        if x == "how many calls?":
            return mf.counter
        elif x == "reset count":
            mf.counter = 0
        else:
            mf.counter += 1
            return f(x)
    return mf

s = make_monitored(sqrt)

print(s(100))
# 10.0
print(s(100))
# 10.0
print(s(100))
# 10.0
print(s("how many calls?"))
# 3
s("reset count")
print(s("how many calls?"))
# 0

# Exercise 3.3 3.4
def make_account(balance, password):
    def withdraw(amount):
        nonlocal balance
        if balance >= amount:
            balance -= amount
            return balance
        else:
            return "Insufficient funds"
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    def dispatch(p, m):
        if not hasattr(dispatch, "alarm"):
            dispatch.alarm = 0
        if p != password:
            dispatch.alarm += 1
            if dispatch.alarm >= 7:
                return lambda x: "Call the cops"
            else:
                return lambda x: "Incorrect password"
        else:
            dispatch.alarm = 0
        if m == "withdraw":
            return withdraw
        elif m == "deposit":
            return deposit
        else:
            raise Exception("Unknown request -- MAKE-ACCOUNT")
    return dispatch
    
acc = make_account(100, "secret password")

print(acc("secret password", "withdraw")(40))
# 60
print(acc("some other password", "withdraw")(50))
# Incorrect password

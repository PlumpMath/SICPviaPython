from scheme_primitive import *

# Exercise 3.7
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
        if p != password:
            return lambda x: "Incorrect password"
        if m == "withdraw":
            return withdraw
        elif m == "deposit":
            return deposit
        else:
            raise Exception("Unknown request -- MAKE-ACCOUNT")
    return dispatch

def make_joint(account, password, new_password):
    def dispatch(p, m):
        if p != new_password:
            return lambda x: "Incorrect password"
        else:
            return account(password, m)
    if is_number(account(password, "withdraw")(0)):
        return dispatch
    else:
        print("Incorrect password")

peter_acc = make_account(100, "open sesame")
paul_acc = make_joint(peter_acc, "open sesame", "rosebud")

# Exercise 3.8
def f(x):
    if not hasattr(f, "state"):
        f.state = 1
    f.state *= x
    return f.state

def g(x):
    if not hasattr(g, "state"):
        g.state = 1
    g.state *= x
    return g.state

print(f(0) + f(1))
# 0
print(g(1) + g(0))
# 1

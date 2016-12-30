# Exercise 3.11

def make_account(balance):
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
    def dispatch(m):
        if m == "withdraw":
            return withdraw
        elif m == "deposit":
            return deposit
        else:
            raise Exception("Unknown request -- MAKE_ACCOUNT")
    return dispatch

# Exercise 3.10

def make_withdraw(initial_amount):
    balance = initial_amount
    def new_func(amount)
        nonlocal balance
        if balance >= amount:
            balance -= amount
            return balance
        else:
            return "Insufficient funds"
    return new_func

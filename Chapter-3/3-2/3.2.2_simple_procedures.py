# Exercise 3.9

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial(n):
    return fact_iter(1, 1, n)

def fact_iter(product, counter, max_counter):
    if counter > max_counter:
        return product
    else:
        return fact_iter(counter * product, counter + 1, max_counter)

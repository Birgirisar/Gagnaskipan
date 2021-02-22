
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base,exp-1)


def multiply(a,b):
    if a == 0:
        return 0
    elif a == 1:
        return b
    else:
        return b + multiply(a-1, b)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * (factorial(n-1))
    

def first_n(n):
    if n == 0:
        return 0
    first_n(n-1)
    print(n, end=' ')


def sum_of_digits(n):
    pass
    
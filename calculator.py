import math


def add(a, b): 
    return a+b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a != "e" or a < 1 or b < 1:
        raise ValueError
    else:
        return math.log(b, a)# use math library + raise ValueError

def exponent(a, b):
    return a ** b


def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError
    else:
        return b/a

def log(a, b):
    if b==0:
        raise ValueError
    else:
        return math.log(b, a)
def exp(a, b):
    return a**b

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""



import math

#try and catch errors for two new functions?
# what does this mean?

#Create your functions right above your add function (with try/catch checking)

def square_root(a):
    try:
        a <0

    except ValueError:
        raise ValueError
    else:
        math.sqrt(a)

def hypotenuse(a, b):
    try:
        math.hypot(a,b)
    except:
        if a < 0:
            a *= -1
            math.hypot(a,b)
        if b < 0:
            b *= -1
            math.hypot(a,b)



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def logarithm(a, b):
    if a != "e" or a < 1 or b < 1:
        raise ValueError
    else:
        return math.log(b, a)# use math library + raise ValueError

def exponent(a, b):
    return a ** b




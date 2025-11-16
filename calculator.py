import math


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
    return a+b



def subtract(a, b):
    return a - b


def logarithm(a, b):
    if a != "e" or a < 1 or b < 1:
        raise ValueError
    else:
        return math.log(b, a)# use math library + raise ValueError






def mul(a,b):
    return a*b

def div(a,b):
    if a==0:
        raise ZeroDivisionError
    else:
        return b/a


def exp(a, b):
    return a**b

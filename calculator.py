#https://github.com/ThunderIconoclast24/lab11-KC-JC.git
#Partner 1: John-Claude Hutchinson
#Partner 2: Kyle Ziegler

import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#Partner 2 functions
def square_root(a):
    try:
        return math.sqrt(a)
        if a<0:
            raise ValueError
    except ValueError:
        raise
def hypotenuse(a,b):
    try:
        if a==0 or b==0:
            raise ValueError
        return math.hypot(a,b)
    except ValueError:
        raise


def add(a:float, b:float):
    return a + b
def subtract(a:float, b:float):
    return a - b
def mul(a:float, b:float):
    return a * b
def div(a:float, b:float):
    try:
        if a == 0:
            raise ZeroDivisionError
        return a/b
    except ZeroDivisionError:
        raise
def logarithm(a:float, b:float):
    try:
        if b <= 0 or a <= 0 or b==1:
            raise ValueError
        return math.log(a,b)
    except ValueError:
        raise

def exp(a:float, b:float):
    return a**b


#git commit -m "modified calculator p1"
#git push
       # configure to merge changes


# First example
#def add(a, b): a+b
#def subtract(a, b): a-b
#def multiply(a, b): a*b


#def logarithm(a,b):raise ValueError if b<=0 or b==1 or a<=0 else math.log(a,b)
#def exponent(a,b):a**b


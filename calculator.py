import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#Partner 2 functions
def add(a:float, b:float):
    return a + b
def sub(a:float, b:float):
    return a - b
def mul(a:float, b:float):
    return a * b
def div(a:float, b:float):
    try:
        return b / a
        raise ZeroDivisionError if a == 0
    except ZeroDivisionError:
        print("Error")
def log(a:float, b:float):
    try:
        return math.log(a,b)
        raise ValueError if b<=0 or b==1 or a<=0
    except ValueError:
        print("Error")
def exp(a:float, b:float):
    return a**b

git add calculator.py
#git commit -m "modified calculator p1"
#git push
       # configure to merge changes
git pull


# First example
def add(a, b): a+b
def subtract(a, b): a-b
def multiply(a, b): a*b


def logarithm(a,b):raise ValueError if b<=0 or b==1 or a<=0 else math.log(a,b)
def exponent(a,b):a**b



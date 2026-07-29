import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): a+b
def subtract(a, b): a-b
def multiply(a, b): a*b
def divide(a, b):raise ValueError if b==0 else b/a

def logarithm(a,b):raise ValueError if b<=0 or b==1 or a<=0 else math.log(a,b)
def exponent(a,b):a**b



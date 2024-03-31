from sympy import *
from sympy.integrals.trigonometry import trigintegrate 

def Diff(f):
    fn=sympify(f)
    x=Symbol('x')
    y=Symbol('y')
    return diff(fn,x)

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

def Taylor(f,o,xn):
    f=sympify(f)
    x = Symbol('x')  
    y0 = f.subs(x,xn)
    yn=y0
    print(yn)
    diffe = Diff(f)
    diff_part = diffe.subs(x,xn)
    print(diffe)

    for i in range(1,o+1):
        yn = yn +((diff_part*((x-xn)**i))/factorial(i))
        diffe = Diff(diffe)
        diff_part = diffe.subs(x,xn)

    return yn


a=input("Enter function:")
b=int(input("Enter number of orders:"))
xn=float(input("enter value of x:"))
x0=float(input("Enter starting value of x"))
Taylor(a,b,xn)
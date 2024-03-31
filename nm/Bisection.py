from sympy import sympify
def bisection(f,a,b,n):
    f=sympify(f)
    var,=f.free_symbols
    fa=f.subs(var,a)
    fb=f.subs(var,b)

    if fa*fb>=0:
        raise ValueError ("Error:The root does not lie in the open interval ")
    print(f'itr   |           a          |          b         |              {var}')
    for i in range(1,n+1):
        x=(a+b)/2
        fx=f.subs(var,x)
        print(f'{i:02}  |  {a:.8f}  |  {b:.8f}  |  {x:.8f}')
        if fx==0:
            print("Root Found: further iteration is not possible")
            break
        elif fx*fa<0:
            b=x
            fb=fx
        else:
            a=x
            fa=fx
    return x
f=input("Enter the function:")
a=float(input("Enter the lower limit:"))
b=float(input("Enter the upper limit:"))
itr=int(input("Enter the number of iterations:"))
print(bisection(f,a,b,itr))

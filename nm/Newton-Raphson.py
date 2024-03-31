from sympy import sympify,diff
def newton(f,x,iterations):
    f=sympify(f)
    var,=f.free_symbols
    df=diff(f)

    print(f'itr|      {var}')
    for i in range(1,iterations+1):
        fx=f.subs(var,x)
        dfx=df.subs(var,x)
        x=float(x-(fx/dfx))
        print(f' {i:02} |  {x:.8f}')
    return x
f=input("Enter the function:")
x0=float(input("Enter the initial guess:"))
itr=int(input("Enter the number of iterations:"))
print(newton(f,x0,itr))


def f(eq,x):
    eq = eq.replace("x",str(x))
    return float (eval(eq))

def simpsons (lower, upper , iterations, eq):
    h = float((upper-lower)/iterations)
    res = f(eq,upper) + f(eq,lower)

    for i in range(1,iterations):
        x=lower+i*h
        if(i%2==0):
            res+=2*f(eq, x)
        else:
            res+=4*f(eq, x)
    return ((float(h)/3)*res)

eq = input("Enter equation:")
u = float(input("Enter upper limit:"))
l = float(input("Enter lower limit:"))
n = int(input("Enter iterations:"))
result=simpsons(l, u, n, eq)

print("Answer:",result)
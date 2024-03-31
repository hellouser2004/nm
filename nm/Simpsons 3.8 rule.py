def f(eq,x):
    eq=eq.replace("x",str(x))
    return float(eval(eq))

def simpsons(lower,upper,iterations,eq):
    h = float((upper-lower)/iterations)
    res = f(eq,upper)+f(eq,lower)

    for i in range(1,iterations):
        x=lower+i*h
        if i%3==0:
            res+=2*f(eq, x)
        else:
            res+=3*f(eq, x)
    return float(3*h/8) * res

eq = input("Enter equation:")
upper=float(input("Enter upper limit:"))
lower=float(input("Enter lower limit:"))
iterations=int(input("Enter interations:"))
res = simpsons(lower, upper, iterations, eq)

print("Answer:",res)
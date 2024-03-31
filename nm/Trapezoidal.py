def f(eq,x):
    eq = eq.replace("x",str(x))
    return float(eval(eq))

def trap(lower, upper, iterations, eq):
    h = float((upper-lower)/iterations)
    res = f(eq, upper) + f(eq, lower)
    for i in range(1,iterations):
        x = lower + i + h
        res += 2*f(eq,x)
        return ((float(h)/2) * res)

eq = input("Enter equations:")
u = float(input("Enter upper limit:"))
l = 

n = int(input("Iterations:"))

result = trap(l, u, n, eq)
print("Answer:", result)
from math import *
def picard(f, y0, x_min, x_max, n):
    h = (x_max - x_min) / (n - 1)
    x = [x_min + i * h for i in range(n)]
    y = [y0] * n

    for i in range(1, n):
        y[i] = y0 + h * sum(f(x[j], y[j]) for j in range(i))
        return x, y

def dy_dx(x, y):
    return x**2 + y

y0 = 3
x_min = 0
x_max = 1
n = 5

x , y = picard(dy_dx, y0, x_min, x_max, n)

for i in range(n):
    print(f"x = {x[i]:.4f}, y = {y[i]:.4f}")
def euler_method(f, x0, y0, h, xn):
  x = [x0]
  y = [y0]
  while x[-1] < xn:
    y_new = y[-1] + h * f(x[-1], y[-1])
    x.append(x[-1] + h)
    y.append(y_new)
  return x, y

def f(x, y):
  return y  # Replace with your actual differential equation

eq_input = input("Enter the differential equation (e.g., dy/dx = y): ")
eq = lambda x, y: eval(eq_input)

x0 = float(input("Enter initial value of x: "))
y0 = float(input("Enter initial value of y: "))
xn = float(input("Enter the value of x for which you want y: "))
h = float(input("Enter the step size: "))

x, y = euler_method(f, x0, y0, h, xn)

print("iter  x      y")
for i, j in zip(x, y):
  print(f"{i:4d}  {x[i]:.4f}  {j:6.4f}")

print(f"Value of y for x = {x[-1]} is {y[-1]}")

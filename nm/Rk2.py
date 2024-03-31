def runge_kutta_2nd(F, x0, y0, h, n):
  eq_input = input("Enter the differential equation in terms of x and y (e.g., y): ")
  eq = lambda X, Y: eval(eq_input)

  x0 = float(input("Enter initial value of x: "))
  y0 = float(input("Enter initial value of y: "))

  h = float(input("Enter step size: "))
  n = int(input("Enter number of iterations: "))

  x_val = [x0]
  y_val = [y0]
  for i in range(1, n + 1):
    K1 = h * F(x_val[i - 1], y_val[i - 1])
    K2 = h * F(x_val[i - 1] + h, y_val[i - 1] + K1)
    Y_new = y_val[i - 1] + 0.5 * (K1 + K2)
    X_new = x_val[i - 1] + h

    x_val.append(X_new)
    y_val.append(Y_new)

  print("Result:")
  for i in range(len(x_val)):
    print("x = ", x_val[i], ", y = ", y_val[i])

  return x_val, y_val

def f(x, y):
  return y

x_val, y_val = runge_kutta_2nd(f, None, None, None, None)

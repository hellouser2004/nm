def runge_kutta_4th(F, x0, y0, h, n):
  eq_input = input("Enter the equation in terms of x & y (e.g., dy/dx = y): ")
  eq = lambda X, Y: eval(eq_input)

  x0 = float(input("Enter initial value of x: "))
  y0 = float(input("Enter initial value of y: "))

  h = float(input("Enter positive step size: "))  # Potential for non-positive input
  n =int(input("Enter number of iterations (integer): "))  # Potential for non-integer input

  x_val = [x0]
  y_val = [y0]

  for i in range(1, n + 1):
    K1 = h * F(x_val[i - 1], y_val[i - 1])
    K2 = h * F(x_val[i - 1] + h / 2, y_val[i - 1] + K1 / 2)
    K3 = h * F(x_val[i - 1] + h / 2, y_val[i - 1] + K2 / 2)
    K4 = h * F(x_val[i - 1] + h, y_val[i - 1] + K3)

    Y_new = y_val[i - 1] + (1 / 6) * (K1 + 2 * K2 + 2 * K3 + K4)
    X_new = x_val[i - 1] + h

    x_val.append(X_new)
    y_val.append(Y_new)

  print("Result:")
  for i in range(len(x_val)):
    print("x = ", x_val[i], ", y = ", y_val[i])

  return x_val, y_val

def f(x, y):
  return y

x_val, y_val = runge_kutta_4th(f, None, None, None, None)

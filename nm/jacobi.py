def jacobi(a, x, b):
    n = len(a)
    x_new = x[:]  # Create a copy of x to store the updated values
    for j in range(n):
        d = b[j]
        for i in range(n):
            if j != i:
                d -= a[j][i] * x[i]
        x_new[j] = d / a[j][j]  # Update x_new instead of x
    return x_new

# Input the number of iterations
num_iterations = int(input("Enter the number of iterations: "))

# Coefficient matrix A
a = [[4, 1, 2],
     [3, 5, 1],
     [1, 1, 3]]

# Constant vector b
b = [4, 7, 3]

# Initial guess for solution vector x
x = [0, 0, 0]

# Perform iterations
for _ in range(num_iterations):
    x = jacobi(a, x, b)

print("Final solution:", x)

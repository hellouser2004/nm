def seidel(a, x, b):     
    n = len(a)                   
    for j in range(0, n):        
        d = b[j]                  
        for i in range(0, n):     
            if j != i:
                d -= a[j][i] * x[i]        
        x[j] = d / a[j][j]          
    return x

# Input the number of iterations
num_iterations = int(input("Enter the number of iterations: "))
n = 3                             
a = [[4, 1, 2],[3, 5, 1],[1, 1, 3]]
b = [4,7,3]
x = [0] * n
for _ in range(num_iterations):            
    x = seidel(a, x, b)
print("Final solution:", x)

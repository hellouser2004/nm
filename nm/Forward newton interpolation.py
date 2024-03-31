def fnewton_interpolation(x,X,Y):
    h=X[1]-X[0]
    u=(x-X[0])/h
    fx=Y[0]
    perm=1
    for i in range(len(X)-1):
        dy=[]
        for j in range(len(Y)-1):
            dy.append(Y[j+1]-Y[j])
        perm*=(u-i)
        fx+=(perm*dy[0])/factorial(i+1)
        Y=dy
    return fx
if _name=='main_':
    x = float(input("Enter the value of x: "))
    X = list(map(float, input("Enter the values of X(comma-separated): ").split(',')))
    Y = list(map(float, input("Enter the values of Y(comma-separated): ").split(',')))
print("Interpolated Value: ", fnewton_interpolation(x, X, Y))

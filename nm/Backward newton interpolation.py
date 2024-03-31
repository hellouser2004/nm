def bnewton_interpolation(x,X,Y):
    h=X[1]-X[0]
    u=(x-X[-1])/h
    fx=Y[-1]
    perm=1
    for i in range(len(X)-1):
        dy=[]
        for j in range(len(Y)-1):
            dy.append(Y[j+1]-Y[j])
        perm*=(u+i)
        fx+=(perm*dy[-1])/factorial(i+1)
        Y=dy
    return fx
if __name__ == '__main__':
    x = float(input("Enter the value of x: "))
    X = list(map(float, input("Enter the values of X(comma-separated): ").split(',')))
    Y = list(map(float, input("Enter the values of Y(comma-separated): ").split(',')))
print("Interpolated Value: ", bnewton_interpolation(x, X, Y))

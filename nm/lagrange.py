from math import prod
def lagrange_interpolation(x,X,Y):
    fx=0
    for i in range(len(X)):
        num=prod(x-X[j] for j in range (len(X)) if j!=1)
        denom=prod(X[i]-X[j] for j in range (len(X)) if j!=i)
        fx+=Y[i]*num/denom
    return fx
if __name__=='__main__':
    x = float(input("Enter the value of x:"))
    X = list(map(float,input("Enter the value of X(comma-separated): ").split(',')))
    Y = list(map(float,input("Enter the value of Y(comma-separated): ").split(',')))
    print("Interpolated value:",lagrange_interpolation(x,X,Y))
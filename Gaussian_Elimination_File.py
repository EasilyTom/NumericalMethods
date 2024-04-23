import numpy as np

def Gaussian_Elimination(A,B,C,f):

    n = len(f)
    # Forward pass
    for i in range(1, n):
        ratio = B[i-1]/A[i-1]
        A[i] -= C[i-1]*ratio
        f[i] -= f[i-1]*ratio
    # Create the solution vector
    x = np.zeros(n, dtype=np.float64)
    # Back pass
    x[-1] = f[-1]/A[-1]
    for i in range(n-2, -1, -1):
        x[i] = (f[i]-(C[i]*x[i+1]))/A[i]
    return x

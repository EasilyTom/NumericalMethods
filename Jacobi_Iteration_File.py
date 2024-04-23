import numpy as np
import numpy.linalg as la


def residual(A, B, C, x, b):
    Ax = np.multiply(A, x)
    Ax[:-1] += np.multiply(C, x[1:])
    Ax[1:] += np.multiply(B, x[:-1])
    return la.norm(b - Ax)


def Jacobi_Iteration(A,B,C,f,x0,epst):
    # Inverse A
    D = np.reciprocal(A)

    # Calculate the minor diagonals of D*B
    DB_sub = np.multiply(D[1:], B)
    DB_sup = np.multiply(D[:-1], C)

    b = np.multiply(D, f)

    x = x0
    resid0 = residual(A,B,C,x,f)
    resid = resid0 + 10
    iter = 0
    while resid > epst*resid0:
        iter += 1

        Mx = np.zeros(len(x), dtype=np.float64)
        Mx[1:] += np.multiply(DB_sub, x[:-1])
        Mx[:-1] += np.multiply(DB_sup, x[1:])

        x = -Mx + b

        resid = residual(A,B,C,x,f)
    return [x, resid, iter]

import numpy as np
def invert_matrix(A): 
    A = np.array(A, dtype=np.float64)
    n_rows, n_cols = A.shape 
    n = n_rows
    if n_rows!= n_cols:
        raise ValueError("Matrix must be square to invert.")
    if n_rows == 1:
        if A[0,0] ==0:
            raise ValueError("Matrix is singular.")
        return np.array([[1/A[0,0]]])

    elif n_rows == 2:
        a, b = A[0,0] , A[0,1]
        c, d = A[1,0] , A[1,1]
        det = a*d - b*c
        if det == 0:
            raise ValueError("Matrix is singular.")
        inv = (1 / det) * np.array([[d,-b],
                                    [-c,a]])
        return inv

    else: n_rows > 2
    ddet = np.linalg.det(A) 
    if ddet == 0:
            raise ValueError("Matrix is singular.") 

    B = np.zeros((n,2*n), dtype=np.float64) 
    B[:, :n] = A 
    B[:, n:] = np.eye(n) 

    for i in range(n): 
        pivot = B[i,i]
        if pivot == 0:
            raise ValueError(f"Zero pivot encountered in row {i}.") 
        B[i,:] = B[i,:] / pivot 

        for k in range(n): 
            if k != i:
                factor = B[k,i]
                B[k,:] = B[k,:] - factor*B[i,:]

    A_inv = B[:,n:] 
    return A_inv

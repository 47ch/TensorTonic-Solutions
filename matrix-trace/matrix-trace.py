import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here

    A = np.array(A)
    sum = 0 
    for i in range(len(A)):
        sum += A[i][i] 

    return sum

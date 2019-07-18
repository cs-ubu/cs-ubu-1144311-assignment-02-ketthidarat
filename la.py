#!/usr/bin/env python3
from mat import *

A = readm('A.csv')
b = readm('b.csv')

def solve(A, b):
    """solve(A,b)
    A - matrix m,k
    b - matrix k,1
    x- list of solution [x_1, x_2, ...,x_n]

    using Gauss Method
    1.กำจัดจุดอ่อน - elimination
    2.แทนค่าย้อนกลับ - back substitution

    """
    # YOUR CODE HERE
    import numpy as np
    A,b = np.array(A), np.array(b)
    n = len(A[0])
    x = np.array([0]*n)
    print(f'n={n}')
    #1.elimination
    for k in range(n-1): #pivot eq
        print(f'เลือกสมการที่ ={k}')
        for j in range(k+1, n):
            #print(f'\tกำจัดสมการตัวแปรที่={k},ออกจากสมการที่={j}')
            lam = A[j][k]/A[k][k]
            # update A[j][k] เป็นต้นไป
            A[j,k+1:n] = A[j,k+1:n] - lam*A[k,k+1:n]
            
            #print(f'\t\tlamda={lam}')

            # update b[j] เป็นต้นไป
            b[j] = b[j] - lam*b[k]
        printm(A)
        print(b)
    
    
    #2.back substitution
    #x[n-1] = b[n-11]/A[n-1][n-1]
    for k in range(n-1, -1, -1):
        print(f'back sub k={k}')
        x[k] = (b[k] - np.dot(A[k,k+1:n], x[k+1:n]))/A[k,k]
    return x.flatten()

print('===A===')
printm(A)
print('===b===')
printm(b)

print( solve(A,b))

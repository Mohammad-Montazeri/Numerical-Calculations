from numpy import *

A = array([[1, 2, 3, 4],
           [2, 3, 4, 1],
           [3, 4, 1, 2],
           [4, 1, 2, 3]])

B = array([[3],
           [0],
           [1],
           [4]])

At = transpose(A)

D = A @ At
D_inv = linalg.inv(D)
X = D_inv @ B

print(X)

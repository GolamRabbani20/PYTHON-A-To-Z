import numpy as np

A=np.array([[1,5,62,58,8],[1,5,9,12,36]])
B=np.array([(2,5,4,6,9,10),(7,8,9,45,3,20)])
print(A.ndim)
print(A.shape)

print(A[0:,2:]+B[0:,0:3])

print(B.ndim)
print(B.shape)
B=B.reshape(6,2)
print(B.shape)
print(B)


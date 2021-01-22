import numpy as np
k = np.array([[1,2],[3,4],[5,6]])
Sum =  k.sum(axis=0)
print(Sum)

Sum1 = k.sum(axis=1)
print(Sum1)

a = np.sqrt(k)
print(a)

#Standard  Deviation
s = np.std(k)
print(s)

a = np.array([[5,6],[10,25]])
b = np.array([[14,45],[20,10]])
print(a + b)
print(a * b)
print(a / b)
print("Matrix multiplication:\n",a.dot(b))
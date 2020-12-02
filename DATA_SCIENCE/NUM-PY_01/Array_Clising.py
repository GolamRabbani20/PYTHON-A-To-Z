import numpy as np

x=np.array([1,2,3,6,5,8,4])
print(x[1:])
print(x[:4])
print(x[::2])
print(x[2:5:2])

print(x[-5:-1])
print(x[-3:])
print(x[:-1])
print(x[-3:-1:-2])


m=np.array([[1,2,3,4,5,6],[7,8,9,10,11,15]])
print("From both elements, return index 2:",m[0:2,2:5:1])

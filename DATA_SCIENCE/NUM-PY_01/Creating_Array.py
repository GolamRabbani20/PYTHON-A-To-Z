import numpy as np
print("Creating an Array:")
print(np.array((2,5,8,355,45,78)))


#0D array
y=np.array(25)
print("\nDimension of the array:",y.ndim)
print(y)

#1D Array

x=np.array([2,36,15,48,7,8,12,65])
print("\nDimension of the array:",x.ndim)
print(x)

#2D array

a=np.array([[2,6,5,9,26,225],[20,125,356,34,56,2,]])
print("\nDimension of the array:",a.ndim)
print(a)

#3D array

arr = np.array([[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]])
print("\nDimension of the array:",arr.ndim)
print(arr)

print("........................................")
r=np.array([2,59,45,30,14,25],ndmin=20)
print(r)
print("Dimension of the array:",r.ndim)


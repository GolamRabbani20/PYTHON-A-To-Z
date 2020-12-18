import numpy as np
arr = np.array([[1,2,3,5],[2,5,8,9]])

k = np.array([1,0,4,5,7,8],ndmin=5)
print(k)
print(k.shape)
print(arr.shape)

p = np.array([10,20,30,5,6,9])
print(p.reshape(2,3))
print(p.reshape(3,2))
print(p.reshape(3,2).base)

new_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = new_arr.reshape(2, 4)
print(x)


_arr = np.array([[1,2,3,4], [10,5,7,8]])
new_array = _arr.reshape(-1)
print("1D array:",new_array)
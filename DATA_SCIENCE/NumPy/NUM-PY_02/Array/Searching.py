import numpy as np
arr1 = np.array([1,2,3,6,5,4,40,5,5,50,5,10])
x = np.where(arr1 == 5)
print(x)

arr2 = np.array([1,2,3,4,5,6,7,8,9,10,12,14])
even = np.where(arr2%2 == 0)
odd = np.where(arr2%2 == 1)
print(even)
print(odd)


arr3 = np.array([1,3,4,5,6,7,10,45,69])
ssort = np.searchsorted(arr3, 10) # searchsorted() function works as binary search
print(ssort)

arr4 = np.array([4,5,7,8,10,15,86,96])
k = np.searchsorted(arr4, 8, side='right')
print(k)

p = np.searchsorted(arr4, [5,15,96])
print(p)
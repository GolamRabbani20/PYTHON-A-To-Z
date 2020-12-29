import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr =  np.array_split(arr, 3)
print(newarr)

arr2 = np.array([1, 2, 3, 4, 5, 6])
newarr2 =  np.array_split(arr, 4)
print(newarr2)

#split can not adjust

arr3 = np.array([7,8,9,10,11,12,13,14])
newarr3 = np.split(arr3,4)
print(newarr3)

#newarr4 = np.split(arr3,5)
#print(newarr4)

arr4 = np.array([1, 2, 3, 4, 5, 6])
newarr4 = np.array_split(arr4, 3)

print(newarr4[0])
print(newarr4[1])
print(newarr4[2])

print("Using loop")
for i in range(3):
    print(newarr4[i])

print("\n2D array")
arr5 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr5 = np.array_split(arr5, 3)
print(newarr5)

for i in range(3):
    print(newarr5[i])

arr6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr6 = np.array_split(arr6, 3)
print(newarr6)

for i in range(3):
    print(newarr6[i])
print('\nnewarr7....................')
arr7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr7 = np.array_split(arr7, 3, axis=1)
print(newarr7)

print('\nnewarr8...................')
arr8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr8 = np.hsplit(arr8, 3)
print(newarr8)

print('\nnewarr9....................')
newarr9 = np.vsplit(arr8, 3)
print(newarr9)

print('\nnewarr10....................')
newarr10 = np.dsplit(arr8, 2)
print(newarr10)
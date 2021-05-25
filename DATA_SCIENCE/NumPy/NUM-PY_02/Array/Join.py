import numpy as np
arr1 =  np.array([1, 2, 3, 5])
arr2 = np.array([10,11,22,45])
arr = np.concatenate((arr1, arr2))
print('Array\n', arr)

#222222222DDDDDDDDDDDDDDDDDDDD

arr3 = np.array([[1,2,3],[5,6,7]])
arr4 = np.array([[3,6,9],[4,67,8]])
arr5 = np.concatenate((arr3,arr4),axis=1)
print('\nArray5\n', arr5)

#1111111111111111111111111111111111111111111111111

arr6 = np.array([1,2,3])
arr7 = np.array([4,5,6])

arr10 = np.stack((arr6, arr7), axis=1)
print('\nArray10\n', arr10)

arr11 = np.hstack((arr6, arr7))
print('\nArray11\n', arr11)

arr12 = np.vstack((arr6, arr7))
print('\nArray12\n', arr12)

arr13 = np.dstack((arr6, arr7))
print('\nArray13\n', arr13)


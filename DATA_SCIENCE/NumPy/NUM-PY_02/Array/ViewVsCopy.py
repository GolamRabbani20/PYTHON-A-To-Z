import  numpy as np
array = np.array([1,5,6,2,65,5])
x = array.copy()
m = array.copy()
array[2] = 50
print(array)
print(x)
print(m)

print("................................")

arr = np.array([20,10,5,6,30])
x = arr.view()
m = x.view()
print("X =",x)
arr[2] = 200
print("Array =",arr)
print("X =",x)
print("M =",m)

print("...................................")

arr1 = np.array([3, 6, 9, 10, 15])
x = arr1.copy()
y = arr1.view()

print(x.base)
print(y.base)


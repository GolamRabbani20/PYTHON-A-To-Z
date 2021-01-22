from numpy import array as ar
x=ar([1,5,6,30,20,45,62,14,78,89])
print(x[3:])
print(x[:4])
print(x[1:6:2])
print(x[2:-1:3])
print(x[-1:0:-2])
print(x[-3:-1])
print(x[4])

arr = ar([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

a= ar([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[78,25,63,5,6]])
print(a[0:3, 1:4])

for cell in arr.flat:
    print(cell)


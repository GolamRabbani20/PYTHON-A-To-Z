import numpy as np
arr =np.array([1,2,3,4])
x=arr.copy()
arr[0]=20
arr[3]=54
print(x)
print(arr)

print(".............................................\n")

m=np.array(['nn','b','c','d',1,2,3,4,5,6])
x=m.view()
x[2]=500
m[0]='roll'
m[8]=100
print(x)
print(m)
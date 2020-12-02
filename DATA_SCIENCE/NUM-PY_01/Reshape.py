import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,14,5,2,56,63,23,6,36,10,12,14,6])
d=int(input("Enter dymension:"))
p=int(input("Enter n of Elements::"))
n=x.reshape(d,3,p)
print(n)




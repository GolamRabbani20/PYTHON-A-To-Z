import numpy as np
x1=[1,2,3]
x2=[4,5,6]
z=np.add(x1,x2)
print(z)

k=[]

for i,j in zip(x1,x2):
    k.append(i+j)

print(k)
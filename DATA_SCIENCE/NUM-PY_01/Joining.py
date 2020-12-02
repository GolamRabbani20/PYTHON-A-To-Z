import numpy as np
x=np.array([[1,2,3],[0,1,2]])
y=np.array([[4,5,6],[0,2,3]])

p=np.concatenate((x,y),axis=1)
print(p)
print()

m=np.array([1,2,3])
n=np.array([4,5,6])

#k=np.stack((m,n))
#k=np.stack((m,n),axis=1)
#k=np.hstack((m,n))  #Stacking Along row
#k=np.vstack((m,n))  #Stacking Along Columns

k = np.dstack((m, n))   #Stacking Along Height (depth)
print(k)
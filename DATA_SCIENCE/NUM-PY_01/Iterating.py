import numpy as np

m=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]],[[1,2,3,4],[5,6,7,8]]])

for k,k1 in np.ndenumerate(m):
    #print("\n2-D array")
    print(k,k1)
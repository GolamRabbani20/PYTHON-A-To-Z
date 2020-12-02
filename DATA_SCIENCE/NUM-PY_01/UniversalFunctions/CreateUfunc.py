import numpy as np
def myadd(x,y,z):
    return x-y+z
myadd=np.frompyfunc(myadd,3,1)

print(myadd([1,2,30],[40,5,6],[5,8,98]))

print(type(np.add))
print(type(np.concatenate))
import numpy as np
try:
  x=np.array([1,2,3,4,5,7])
  k=np.array_split(x,4)

  print(k[0])
  print(k[1])
  print(k[2])

  print(k[4])
except IndexError:
    print("n0")
#One 2-D array to three 2-D array
v=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
#h=np.array_split(v,3,axis=1)
#h=np.hsplit(v,3)
#h=np.vsplit(v,3)
#h=np.vsplit(v,3)
#h=np.dsplit(v,3)
h=np.vstack(v,3)
print(h)
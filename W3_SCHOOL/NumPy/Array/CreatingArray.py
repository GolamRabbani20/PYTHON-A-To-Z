from numpy import array as ar
a=ar(20)  #0D
p=ar((1,3,5,6,9,8))
print(p)

b=ar([1,2,10,45]) #1D
c=ar([[1,2,4,5],[7,8,95,2]]) #2D
d=ar([[[1,2,34,40],[7,89,90,45]],[[8,11,9,47],[14,78,96,10]]]) #3D
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(d[1][0])
print(d[0][1][1::2])


x=ar([1,4,5,2],ndmin=5)
print(x)
print(x.ndim)
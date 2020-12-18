from numpy import array as ar
x=ar([1,5,8,9,6,5])
print(x[5]+x[3])
m=ar([[4,5,6,3,58],[8,4,75,6,10]])
print(m[1,2])
print(m[0,4])

m=ar((1,2,5,6,9))
print("vale=",m[2])

k=ar([[[4,6,8,9,6],[1,4,5,2,6],[4,5,6,3,10]],[[7,8,9,0,4],[3,10,4,7,9],[7,89,6,3,2]]])
print(k.ndim)
print(k[1,2,4])
print(k[-1,-1,-3])
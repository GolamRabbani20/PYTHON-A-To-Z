import numpy as np

A=np.array([[1,5,62,58,8],[1,5,9,12,36]])
B=np.array([(2,5,4,6,9,10),(7,8,9,45,3,20)])
print(A.ndim)
print(A.shape)

print(A[0:,2:]+B[0:,0:3])

print(B.ndim)
print(B.shape)
B=B.reshape(6,2)
print(B.shape)
print(B)

print("\n111........................................................\n")
a = np.arange(12).reshape(3,4)
print(a)
b = np.arange(12,24).reshape(4,3)
print(b)

print("a x b = \n",a.dot(b))

print("\n222.........................................................\n")
w=np.vstack((a,b.reshape(3,4)))
print(w)
print(np.hstack((a,b.reshape(3,4))))
print("\n333.........................................................\n")

big = np.arange(30).reshape(2,15)
print(big)
result = np.hsplit(big,3)

print("\n444.........................................................\n")
for i in result:
    print(i,'\n')

print("\n555.........................................................\n")
result1 =  np.vsplit(big,2)
print(result1[0])
print(result1[1])

print("\n666.........................................................\n")
x = np.arange(12).reshape(3,4)
print(x,'\n')
test = x > 4
print(test,'\n')

print(x[test],'\n')

x[test] = -1
print(x)

print("\n777.........................................................\n")
m = np.arange(20).reshape(4,5)
print(m,'\n')

for cell in m.flatten():
    print(cell,end=" ")

for cell1 in np.nditer(m,order='C'):  # C order mane row wise print korbe
    print(cell1)
print("\nFortran order")
for cell1 in np.nditer(m,order='F'):  # F = Fortran order that means column by column
    print(cell1,end=" ")

print("\n\n888.........................................................")
for k in np.nditer(m,order='F',flags=['external_loop']):
    print(k)

print("\nChange Original array:\n")
for c in np.nditer(m,op_flags=['readwrite']):
     c[...]=c*c
print(m)

print("\nBroadcasting.................................................")
n = np.arange(12).reshape(3,4)
p = np.arange(3,15,4).reshape(3,1)
for i,j in np.nditer([n,p]):
    print(i,j)
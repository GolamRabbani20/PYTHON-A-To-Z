import numpy as np
'''
x=[]
for i in range(3):
    x.append(int(input("Enter Elements:")))

k=np.array(x)
print(np.arange(0,10))
print(type(k))
print(k)
'''
print(np.zeros((3,5)))
p=np.ones((3,10,8))
print(p)

u=np.full((3,4),10)
print(u)

e=np.eye(5)
print(e)

y=np.linspace(-1,2,10)
print(y)

l=np.logspace(0,14,5,base=np.e)
print(l)

m=np.diag([1,2,3])
print(m)

j=np.random.rand(2,10,5)
print(j)
print()
v=np.random.randn(3,5)
print(v)
print()

h=np.random.randint(1,20,(3,4),dtype="int")
print("\nH1=",h)

print("\nH2=",h.reshape(2,6))

print("Max=",h.max(),"Min=",h.min(),"\nIndex of Max=",h.argmax())
print("Item size=",h.itemsize)
print("Size of h=",h.size)
print("Memory Address=",h.data)

g=np.arange(0,20)
print("Range=",g)
print("Max=",g.max())
print("Min=",g.min())
print("Index of max:",g.argmax())
print()

d2=np.random.randint(0,100,(4,5))
print(d2)
print()

print(d2[1:3,2:5])

d3=np.arange(0,10)
print(d3)
print(d3>5)
print()

k1=d3[d3>5]
print(k1)

a1=np.arange(1,21).reshape(4,5)
a2=np.arange(21,41).reshape(4,5)
print()
print(a1)
print()
print(a2)
print()
print(a1+a2)
print()
print("Add by Universal function:\n",np.add(a1,a2))
print("Square root:\n",np.sqrt(a1))
print("\n",a1*a2)
print('\n',a2/a1)


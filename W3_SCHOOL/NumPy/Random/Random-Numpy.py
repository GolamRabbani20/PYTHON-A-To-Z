from numpy import random
import uuid

x=random.rand()
print(x)

y=random.randint(50,size=5)
print("1D array=",y)
for i in range(1,6):
    z=random.randint(20,100,size=(5,7))

    print("\n2D Array",i)
    print(".....................")
    print(z)
for c in range(10):
   m=random.choice([5,6,20,3,23,255,62,30])
   print(m)

p=random.random(5)
print("P=",p)

k=random.uniform(20.5,30.5)
print(k)

j=uuid.uuid1()
print(j)

g=hex(uuid.getnode())
print(g)


print("X=",uuid.NAMESPACE_DNS)


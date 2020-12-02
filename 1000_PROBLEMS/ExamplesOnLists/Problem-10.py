#Python Program to Create a List of Tuples with the First Element as the Number
# and Second Element as the Square of the Number
m=int(input("Enter lower range:"))
n=int(input("Enter upper range:"))
x=[]
a=[(x,x*x) for x in range(m,n+1)]
print(a)

for i in range(m,n+1):
    x.append(tuple((i,i*i)))
print(x,)

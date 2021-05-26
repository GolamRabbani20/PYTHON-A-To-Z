#Python Program to Multiply All the Items in a Dictionary
n = int(input("Enter size:"))
x={}
for i in range(n):
    k=int(input("Enter key:"))
    v=int(input("Enter value:"))
    x.update({k:v})
mul=1
for m in x.values():
    mul*=m
print("Multiply of values:",mul)

#...............................................

p={'A':20,'B':50,'C':60,'D':100}
total=1
for i in p.values():
    total*=i
print("Total=",total)
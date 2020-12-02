#Python Program to Find the Second Largest Number in a List
n=int(input("Enter list size:"))
x=[]
for i in range(n):
    a=int(input("Enter a element:"))
    x.append(a)
x.sort()
print("The largest value in the list:",x[n-2])
#Python Program to Find the Second Largest Number in a List Using Bubble Sort
n=int(input("Enter list size:"))
x=[]
for i in range(n):
    x.append(int(input("Enter element:")))

for k in range(0,n):
    for j in range(0,n-k-1):
       if x[j]>x[j+1]:
           temp=x[j]
           x[j]=x[j+1]
           x[j+1]=temp

print("Second largest number is:",x[n-2])


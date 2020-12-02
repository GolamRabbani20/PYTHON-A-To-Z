#Python Program to Print Largest Even and Largest Odd Number in a List
n=int(input("Enter list size:"))
a=[]
for i in range(1,n+1):
    a.append(int(input("Enter element:")))

b=[]
c=[]

for j in a:
    if j%2==0:
        b.append(j)
    else:
        c.append(j)


count1=0
count2=0

c.sort()
b.sort()

for k in b:
    count1 += 1
for m in  c:
    count2 += 1
print("Larest even in the list:",b[count1-1])
print("Largest odd in the list:",c[count2-1])

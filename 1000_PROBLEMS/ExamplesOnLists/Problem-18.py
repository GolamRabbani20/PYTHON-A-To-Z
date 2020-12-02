#Python Program to Remove the ith Occurrence of the Given Word in a List where Words can Repeat
n=int(input("Enter list size:"))
x=[]
for i in range(n):
    x.append(input("Enter a word"+str(i+1)+":"))
print("The Original list is:",x)

c=0
y=[]

m=input("Enter a word to remove:")
a=int(input("Enter number of occurrence:"))

for k in x:
    if k==m:
        c=c+1
        if a!=c:
            y.append(k)
    else:
        y.append(k)
if c==0:
    print("Item not found!")
else:
    print("Number of repetitions:",c)
    print("Update list:",y)
    print("Non repeat list:",set(x)) #set does not accept duplicate valu


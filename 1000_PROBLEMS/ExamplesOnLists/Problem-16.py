#Python Program to Remove the Duplicate Items from a List
n=int(input("Enter number of elements:"))
x=[]
y=[]
for i in range(n):
    x.append(int(input("Enter element:")))

for k in x:
    if k not in y:
        y.append(k)
print("The non duplicate items:",y)
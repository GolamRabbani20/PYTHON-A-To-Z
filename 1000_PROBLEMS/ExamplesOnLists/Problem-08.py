#Python Program to Find the Union of two Lists
x=[]
y=[]
n=int(input("Enter list size1:"))
for i in range(n):
    x.append(int(input("Enter Element list1:")))

m=int(input("Enter list size2:"))
for k in range(m):
    y.append(int(input("Enter Element for list2:")))
#p=set.intersection(set(x),set(y))
#print("The intersection of two list:",p)
Union=list(set().union(x,y))
print("The Union of two list:",Union)





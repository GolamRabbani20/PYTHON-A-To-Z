#Python Program to Merge Two Lists and Sort it
n=int(input("Enter list size:"))
x=[]
y=[]
marge=[]

for i in range(n):
       print("Iteration:",i+1)
       m=int(input("Enter elements for list1:"))
       x.append(m)
       k=int(input("Enter elements for list2:"))
       y.append(k)

marge=x+y
marge.sort()
print("The final list is:",marge)
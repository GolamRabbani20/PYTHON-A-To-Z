#Python Program to Put Even and Odd elements in a List into Two Different Lists
n=int(input("Enter list size:"))
Even=[]
Odd=[]
for i in range(n):
    x=int(input("Enter elements:"))
    if x%2:
        Even.append(x)
    else:
        Odd.append(x)

print("The Even list is:",Even)
print("The Odd list is:",Odd)

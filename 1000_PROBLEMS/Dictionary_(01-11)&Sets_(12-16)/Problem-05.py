#Python Program to Sum All the Items in a Dictionary
n=int(input("Enter a number:"))
m={x:x*x*x for x in range(1,n+1)}

print("The dictionary:",m)
print("Sum of keys:",sum(m.keys()))
print("Sum of values:",sum(m.values()))
print("Sum of keye & values:",sum(m.keys())+sum(m.values()))
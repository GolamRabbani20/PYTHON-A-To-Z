#Python Program to Map Two Lists into a Dictionary
n=int(input("Enter size:"))
key=[]
value=[]
for i in range(n):
    key.append(int(input("Enter key-"+str(i+1)+":")))
for k in  range(n):
    value.append(input("Enter value-"+str(k+1)+":"))

print(dict(zip(key,value)))
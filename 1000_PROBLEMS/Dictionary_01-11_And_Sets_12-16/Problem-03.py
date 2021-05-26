#Python Program to Check if a Given Key Exists in a Dictionary or Not
x=int(input("Enter size:"))
m={}
for i in range(x):
    k=int(input("Enter key:"))
    v=input("Enter value:")
    m.update({k:v})
n=int(input("Enter a key:"))
if n in m.keys():
    print("The key is exists and value is:",m[n])
else:
    print("No")
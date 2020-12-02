#Python Program to Search the Number of Times a Particular Number Occurs in a List
n=int(input("Enter the number of elements:"))
c=0
x=[]
for i in range(n):
    x.append(int(input("Enter the element:")))

m=int(input("Enter a search element:"))
#print("Result=",x.count(m))

for k in x:
    if k==m:
      c=c+1
print(m,"is",c,"times occurs.")


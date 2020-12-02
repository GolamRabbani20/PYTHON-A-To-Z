#Python Program to Read a Mumber n and Compute n+nn+nnn=5+55+555=615
n=int(input("Enter the value of n:"))
s=str(n)
x=s+s
y=s+s+s
sum=n+int(x)+int(y)
print("The result is:",sum)

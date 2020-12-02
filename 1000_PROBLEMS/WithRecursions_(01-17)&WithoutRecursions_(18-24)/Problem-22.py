#Python Program to Find the Binary Equivalent of a Number without Using Recursion
n=int(input("Enter a number:"))
#p=bin(n)
#print(p[2:])
x=[]
while n!=0:
    x.append(n%2)
    n=n//2
x.reverse()
for k in x:
    print(k,end="")
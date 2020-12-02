#Python Program to Find the Binary Equivalent of a Number Recursively
p=[]
def birary(n):
    if n==0:
        return 1

    p.append(n%2)

    birary(n//2)

x=int(input("Enter a number:"))
birary(x)
p.reverse()
for i in p:
    print(i,end="")
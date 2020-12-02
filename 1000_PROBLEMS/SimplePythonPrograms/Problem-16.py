#Python Program to Read a Number n And Print the Series “1+2+…..+n= “
n=int(input("Enter a number:"))
a=[]

for i in range(1,n+1):
    print(i,sep=" ",end=" ")
    if i<n:
      print("+",end=" ")
    a.append(i)
print("=",sum(a))
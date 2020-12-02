#Python Program to Read a Number n and Print the Natural Numbers Summation Pattern
n=int(input("Enter a number:"))
for i in range(1,n+1):
    x=[]
    for j in range(1,i+1):
        print(j,sep=" ",end=" ")
        if j<i:
            print("+",sep=" ",end=" ")
        x.append(j)
    print("=",sum(x))
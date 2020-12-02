#Python Program to Print an Identity Matrix
m=int(input("Enter the order of matrix:"))

for i in range(1,m+1):
    for j in range(1,m+1):
        if i==j:
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")

    print()


for k in range(1,m+5):
   print(".",end=" ")
print("\n")


for i in range(1,m+1):
    for j in range(1,m+1):
        if i==j:
            print("0",sep=" ",end=" ")
        else:
            print(j,sep=" ",end=" ")

    print()
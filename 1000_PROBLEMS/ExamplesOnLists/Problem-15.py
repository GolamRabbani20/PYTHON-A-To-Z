#Python Program to Swap the First and Last Value of a Lis
n=int(input("Enter number of elements:"))
x=[]
for i in range(n):
    x.append(int(input("Enter element:")))
temp=x[0]
x[0]=x[n-1]
x[n-1]=temp
print("The list is:",x)
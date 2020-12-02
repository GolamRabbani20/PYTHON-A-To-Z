#Python Program to Sort a List According to the Length of the Elements
n=int(input("Enter list size:"))
x=[]
for i in range(n):
    x.append(input("Enter element in string:"))
#x.sort(key=len)
#print(x)
for j in range(0,n):
    for k in range(0,n-j-1):
        if len(x[k])>len(x[k+1]):
            temp=x[k]
            x[k]=x[k+1]
            x[k+1]=temp
print(x)

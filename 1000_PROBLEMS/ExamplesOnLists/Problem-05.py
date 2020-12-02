#Python Program to Sort the List According to the Second Element in Sublist
x=[['A',40],['D',25],['B',35],['E',30],['C',15]]
n=len(x)

for i in range(0,n):
    for j in range(0,n-i-1):
        if (x[j][1]>x[j+1][1]):
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp
print("Sort the List According to the Second Element:",x)

for i in range(0,n):
    for k in range(0,n-i-1):
        if (x[k][0]>x[k+1][0]):
            temp1=x[k]
            x[k]=x[k+1]
            x[k+1]=temp1
print("\nSort the List According to the First Element:",x)

#Python Program to Find the Sum of the Series: 1 + 1/2 + 1/3 + ….. + 1/N
n=int(input("Enter a number:"))
sum1=0
for i in range(1,n+1,1):
    sum1=sum1+(1/i)
print("Sum of the Series:",round(sum1,3))
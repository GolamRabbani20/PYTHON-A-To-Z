#Python Program to Find the Sum of First N Natural Numbers
n=int(input("Enter a number:"))
sum1=0
for i in range(1,n+1,1):
    sum1+=i
print("Sum of First N Natural Numbers:",sum1)
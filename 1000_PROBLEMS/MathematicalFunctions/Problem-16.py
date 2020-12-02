#Python Program to Check if a Number is a Strong Number
n=int(input("Enter a number:"))
m=n
sum=0
while n:
    i=1
    f=1
    rem=n%10
    while i<=rem:
       f=f*i
       i=i+1
    sum=sum+f
    n=n//10
if sum==m:
    print(sum,"is a strong number.")
else:
    print(m,"is not a strong number!")


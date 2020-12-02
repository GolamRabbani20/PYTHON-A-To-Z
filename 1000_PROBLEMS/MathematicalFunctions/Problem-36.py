#Python Program to Find Whether a Number is a Power of Two
n=int(input("Enter the value of n:"))
s=0
for i in range(1,n):
    if (2**i==n):
        s=s+1
        break
if s==0:
    print(n, "is not power of two")
else:
    print(n, "is power of two")
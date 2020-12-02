#Python Program to Check if a Number is a Perfect Numbe
n=int(input("Enter a number:"))
x=0
for i in range(1,n):
   if n%i==0:
      x+=i
if x==n:
    print(x,"is the perfect number!")
else:
    print(n,"is not a perfect number!")


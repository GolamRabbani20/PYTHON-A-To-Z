#Python Program to Check if a Number is an Armstrong Number
n=int(input("Enter a number:"))
''''
m=n
s=0
while n>=1:
    rem=n%10
    rem=rem**3
    s=s+rem
    rem=0
    n=n//10


if s==m:
    print("The number is Armstrong!")
else:
    print("The number is not Armstrong!")
'''
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if (sum(b)==n):
    print("The number is an Armstrong!")
else:
    print("The number is not an Armstrong!")

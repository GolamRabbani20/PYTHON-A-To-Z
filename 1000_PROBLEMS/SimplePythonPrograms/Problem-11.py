#Python Program to Find the Sum of Digits in a Number
x=int(input("Enter a number:"))
sum=0
while x>=1:
    rem=x%10
    sum=sum+rem
    x=x//10
print("Sum of digits=",sum)
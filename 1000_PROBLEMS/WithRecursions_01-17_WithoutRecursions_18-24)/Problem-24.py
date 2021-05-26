#Python Program to Find the Sum of Digits in a Number without Recursion
n=int(input("Enter a number:"))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print("The sum of digits:",s)
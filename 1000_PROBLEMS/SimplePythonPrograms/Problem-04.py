#Python Program to Reverse a Given Number
x=int(input("Enter a number:"))
rev=0
while x>0:
    rem=x%10
    rev=rev*10+rem
    x=x//10
print(rev)
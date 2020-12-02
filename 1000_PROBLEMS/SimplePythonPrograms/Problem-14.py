#Python Program to Check if a Number is a Palindrome
n=int(input("Enter a number:"))
temp=n
p=0

while n>=1:
    rev=n%10
    p=p*10+rev
    n=n//10

if (temp==p):
      print("The number is palindrome !")
else:
    print("The number is not palindrome !")
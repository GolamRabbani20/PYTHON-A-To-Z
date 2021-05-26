#Python Program to Check Whether a String is a Palindrome or not Using Recursion
def palindrome(s):

    if len(s)<1:
        return True
    else:
        if s[0]==s[-1]:
           return palindrome(s[1:-1])
        else:
           return False

x=input("Enter a string:")

if palindrome(x)==True:
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")

#Python Program to Check if a String is a Palindrome or Not
x=input("Enter a string:")

if x==x[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
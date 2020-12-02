#Python Program to Reverse a String without using Recursion
s=input("Enter a string:")
#print(s[::-1])

for k in reversed(s):
    print(k,end="")
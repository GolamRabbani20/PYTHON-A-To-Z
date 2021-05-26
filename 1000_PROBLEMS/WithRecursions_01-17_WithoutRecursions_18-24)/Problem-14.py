#Python Program to Reverse a String Using Recursion
def rev(s):
   if len(s)==0:
       return s
   return rev(s[1:])+s[0]

n=input("Enter a string:")
print("The new string is:",rev(n))

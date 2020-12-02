#Python Program to Detect if Two Strings are Anagrams
x=input("Enter 1st string:")
y=input("Enter 2nd string:")
if sorted(x)==sorted(y):
    print("The Strings are Anagrams")
else:
    print("The Strings are not Anagrams")
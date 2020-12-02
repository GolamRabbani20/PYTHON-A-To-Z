#Python Program to Check if a Substring is Present in a Given String
s=input("Enter a sentence:")
sub_s=input("Enter a sub string:")
if (s.find(sub_s)==-1):
    print("The word not found!")
else:
    print("The word is found!")

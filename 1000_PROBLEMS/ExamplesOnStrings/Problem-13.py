#Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String
n=input("Enter string:")
l=0
u=0
for x in n:
    if (x.islower()):
        l=l+1
    elif (x.isupper()):
          u=u+1
print("Number of lower case:",l)
print("Number of upper case:",u)
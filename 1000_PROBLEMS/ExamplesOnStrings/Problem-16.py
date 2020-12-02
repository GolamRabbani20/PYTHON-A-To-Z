#Python Program to Calculate the Number of Digits and Letters in a String
s=input("Enter a string:")
d=0
l=0
'''
for i in s:
    if i>='0' and i<='9':
        d=d+1
    elif i>='a' and i<='z' or i>='A' and i<='Z':
        l+=1
print("Number digits=",d)
print("Number of letter=",l)
'''
for x in s:
    if (x.isdigit()):
        d+=1
    elif x.isalpha():
         l+=1
print("Number digits=",d)
print("Number of letter=",l)
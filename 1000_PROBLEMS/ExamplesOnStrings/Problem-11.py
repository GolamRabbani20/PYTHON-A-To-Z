#Python Program to Count Number of Lowercase Characters in a String
x=input("Enter a string:")
count1=0
for i in x:
    #if i>='a' and i<='z':
        #count1+=1
    if (i.islower()):
        count1+=1

print("Number of lower case character in the string is:",count1)
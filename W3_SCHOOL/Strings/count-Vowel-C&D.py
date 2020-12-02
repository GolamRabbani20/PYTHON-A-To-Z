str=input("Enter a string:")
v=0
d=0
c=0
sp=0
for i in str:
    if (i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        v+=1
    elif i>='0' and i<='9':
        d+=1
    elif i==" ":
        sp+=1
    else:
        c+=1
print("Vowel=",v,"\nConsonant=",c,"\nDigits=",d)

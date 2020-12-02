#Python Program to Find the LCM of Two Numbers
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

if a>b:
    max1=a
else:
    max1=b

while(1):
    if max1%a==0 and max1%b==0:
        print("The LCM is:",max1)
        break
    max1=max1+1
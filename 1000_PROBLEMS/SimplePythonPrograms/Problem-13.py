#Python Program to Count the Number of Digits in a Numbe
x=int(input("Enter a number:"))
s=0
while x>=1:
    rem=x%10
    s+=1
    x=x//10
print("Total number of digits:",s)
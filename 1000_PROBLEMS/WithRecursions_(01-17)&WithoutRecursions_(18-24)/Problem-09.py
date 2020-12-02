#Python Program to Find the GCD of Two Numbers Using Recursion
def gcd(a,b):
    if a!=0:
       return gcd(b%a,a)
    return b

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if a<b:
    print("LCD=",gcd(a,b))
    print("LCD=",(a*b)//gcd(a,b))
else:
    print("LCD=",gcd(b,a))
    print("LCD=", (a * b) // gcd(a, b))
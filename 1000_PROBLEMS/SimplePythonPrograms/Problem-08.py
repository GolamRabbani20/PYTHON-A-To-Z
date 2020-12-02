#Python Program to Read Two Numbers and Print Their Quotient and Remainder
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
if x<y:
    q=y/x
    rem=y%x
    print("Quotient:",q)
    print("Remainder:",rem)
else:
    q = x // y
    rem = x % y
    print("Quotient:", q)
    print("Remainder:", rem)

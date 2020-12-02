#Python Program to Find the Product of two Numbers Using Recursion
def product(a,b):
    if b<a:
       return product(b,a)
    if a!=0:
        return b+product(a-1,b)
    else:
        return 0

a=int(input("Enter 1st number:"))
b=int(input("Enter 2st number:"))
print("The product is:",product(a,b))
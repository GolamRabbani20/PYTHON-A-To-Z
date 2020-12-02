#Python Program to Find the Power of a Number Using Recursion
def fun(b,p):
    if p>=1:
        return b*fun(b,p-1)
    return 1

b=int(input("Enter base:"))
p=int(input("Enter exponential value:"))
print("Result =",fun(b,p))
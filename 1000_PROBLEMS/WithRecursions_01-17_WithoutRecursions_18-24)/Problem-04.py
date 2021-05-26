#Python Program to Find the Factorial of a Number Using Recursion
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
x=int(input("Enter a number:"))
print("The factorial of the number:",fact(x))
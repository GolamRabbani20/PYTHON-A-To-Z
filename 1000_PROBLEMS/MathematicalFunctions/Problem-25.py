#Python Program to Print Numbers in a Range (1,upper) Without Using any Loops
def p(n):
    if n>0:
        p(n-1)
        print(n)
n=int(input("Enter a number:"))
p(n)

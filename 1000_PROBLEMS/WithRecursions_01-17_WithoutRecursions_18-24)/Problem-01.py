#Python Program to Determine Whether a Given Number is Even or Odd Recursively
def evenOrOdd(n):
    if n<2:
        return n%2==0
    return evenOrOdd(n-2)

x=int(input("Enter a number:"))
print(evenOrOdd(x))
if evenOrOdd(x)==True:
    print("The number is even!")
else:
    print("The number is odd!")
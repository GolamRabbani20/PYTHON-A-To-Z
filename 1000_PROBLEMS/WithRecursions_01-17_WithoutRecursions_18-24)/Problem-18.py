#Python Program to Find the Fibonacci Series without Using Recursion
first=int(input("Enter 1st number:"))
second=int(input("Enter 2nd number:"))
n=int(input("Enter number of term:"))

print(first,second,end=" ")
for k in range(n-2):
    fibo=first+second
    first=second
    second=fibo
    print(fibo,end=" ")
#Python Program to Find the Fibonacci Series Using Recursion
def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

x=int(input("Enter a number:"))

for i in range(x):
    print(fibo(i),end=" ")
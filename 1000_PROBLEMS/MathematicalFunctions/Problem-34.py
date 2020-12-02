#Python Program to test Collatz Conjecture for a Given Number
def collatz(n):
    print(n,end="\t")
    while n>1:
        if n%2:
            n=3*n+1
        else:
            n=n//2
        print(n,end="\t")

n=int(input("Enter a value of n:"))
collatz(n)
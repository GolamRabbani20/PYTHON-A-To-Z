#Python Program to Find if a Number is Prime or Not Prime Using Recursion
def prime(n,i=2):
    if i<n:     #i=n-1    if i>=2: return prime(n,i-1)
       if n%i!=0:
          return prime(n,i+1)
       else:
           return 0
    else:
      return 1

n=int(input("Enter a number:"))

if prime(n)==1:
    print("The number is prime")
else:
    print("The number is not prime")
#Python Program to Read Print Prime Numbers in a Range using Sieve of Eratosthenes
n=int(input("Enter a number:"))
t=0
sieve=set(range(2,n+1))
while sieve:
    prime=min(sieve)
    print(prime,end="\t")
    t+=1
    sieve=sieve-set(range(prime,n+1,prime))
    #print("Sieve:",sieve)
print()
print("Total Prime numbers=",t)



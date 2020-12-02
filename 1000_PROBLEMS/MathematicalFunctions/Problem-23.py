#Python Program to Check if a Number is a Prime Number
n=int(input("Enter a number:"))
s=0
k=2
x=[]
y=[1,]
s1=0
s2=0
while k<=n:
   for i in range(2,k):
       if k%i==0:
           s=s+1
           break
   if s==0:
       x.append(k)
       s1+=1

   else :
      y.append(k)
      s2+=1
   k+=1
   s=0
print("List of Prime numbers:",x,"=",s1,"## Summation of primes=",sum(x))
print("List of non prime numbers:",y,"=",s2+1,"## Summation of non primes=",sum(y)+1)
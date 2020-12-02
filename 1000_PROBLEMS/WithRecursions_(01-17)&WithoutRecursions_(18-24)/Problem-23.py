#Python Program to Find All Numbers which are Odd and Palindromes Between a Range of Numbers without using Recursion
n=int(input("Enter lower range:"))
m=int(input("Enter upper range:"))
x=[k for k in range(n,m+1) if k%2!=0 and str(k)==str(k)[::-1]]
print("All odd palindromes in the range:",x)

p=[i for i in range(n,m+1) if i%2==0 and str(i)==str(i)[::-1]]
print("All even palindromes in the range:",p)

'''
x=[]
s=0
for k in range(n,m+1):
    p=k
    while k>=1:
         r=k%10
         s=s*10+r
         k=k//10
    if p%2!=0 and p==s:
        x.append(s)
    s=0
print("The numbers are:",x)
'''
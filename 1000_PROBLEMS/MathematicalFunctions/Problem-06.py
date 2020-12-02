#Python Program to Compute Prime Factors of an Integer
"""
a=int(input("Enter a number:"))
s=[]
for i in range(2,a+1):
    if a%i==0:
        s.append(i)

"""
n=int(input("Enter an integer:"))
print("Prime Factors are:")
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1
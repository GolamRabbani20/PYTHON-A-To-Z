#Python Program to Generate all the Divisors of an Integer
a=int(input("Enter a number:"))
s=[]
for i in range(1,a+1):
    if a%i==0:
        s.append(i)
print(s)
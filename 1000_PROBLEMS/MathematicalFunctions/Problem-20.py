#Python Program to Check If Two Numbers are Amicable Numbers
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
sum1=0
sum2=0

for i in range(1,a):
    if a%i==0:
        sum1+=i
for k in range(1,b):
    if b%k==0:
        sum2+=k
if sum1==b and sum2==a:
    print("Amicable")
else:
    print("Not Amicable")

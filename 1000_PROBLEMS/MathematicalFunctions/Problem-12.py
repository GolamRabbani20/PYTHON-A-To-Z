#Python Program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers
m=int(input("Enter lower range:"))
n=int(input("Enter upper range:"))
x=[]
for i in range(m,n):
    if i%5==0 and i%7==0:
        x.append(i)
print("The numbers which divisible by 5 & 7 is :",x)

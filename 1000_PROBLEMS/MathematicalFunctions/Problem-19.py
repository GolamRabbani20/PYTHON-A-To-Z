#Python Program to Compute a Polynomial Equation given that the Coefficients of the Polynomial are stored in a List
print("Equation is : ax^n + bx^n-1 + cx^n-2 +.....+ dx^n-(n-1) + constant")
a=[]
n=int(input("Enter number of element:"))
for i in  range(n):
    if i !=n-1:
       a.append(int(input("Enter a coefficient:")))
    else:
        a.append(int(input("Enter constant value:")))

x=int(input("Enter value of x:"))
sum1=0
p=n-1
for k in range(0,n-1):
    while p>0:
        sum1=sum1+(a[k]*(x**p))
        break
    p-=1
sum1+=a[n-1]
print("The result of polynomial is:",sum1)

'''
import math
print("The coefficient form is ax^3 + bx^2 + cx + d")
a=[]
for i in range(0,4):
    a.append(int(input("Enter a coefficient:")))
x=int(input("Enter a value of x:"))

sum1=0
j=3
for k in  range(0,3):
    while (j>0):
        sum1=sum1+(a[k]*math.pow(x,j))
        break
    j=j-1
sum1=sum1+a[3]
print("Result is of polynomial equation:",sum1)

'''
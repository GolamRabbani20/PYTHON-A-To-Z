#Python Program to Find the Sum of the Series: 1 + x^2/2 + x^3/3 + … x^n/n
n=int(input("Enter number of term:"))
x=int(input("Enter value of x:"))
s=1
for i in range(2,n+1):
    s=s+(x**i)/i

print("Sum of the Series:",round(s,2))
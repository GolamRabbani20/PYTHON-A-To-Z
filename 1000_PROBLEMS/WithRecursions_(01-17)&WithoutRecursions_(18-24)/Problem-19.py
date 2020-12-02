#Python Program to find the factorial of a number without recursion
n=int(input("Enter a number:"))
m=1
for k in range(1,n+1):
    m=m*k
print("The result is:",m)
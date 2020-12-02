#Python Program to Compute the Value of Euler’s Number e. Use the Formula: e = 1 + 1/1! + 1/2! + …… 1/n!
import math
n=int(input("Enter number of term:"))
s=1
for i in range(1,n+1):
    s=s+(1/math.factorial(i))
print("Result of  the Formula:",round(s,2))
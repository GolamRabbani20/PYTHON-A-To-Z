#Python Program to Find the Sum of Cosine Series
import math
def cos(x,n):
    pi=22/7
    r=(pi/180)*x
    cosine=0
    for i in range(n):
        sign=(-1)**i
        cosine=cosine+((r**(i*2))/math.factorial((i*2)))*sign
    return cosine

x=int(input("Enter degree of cos:"))
n=int(input("Enter number of term:"))
m=cos(x,n)
print("Result is=",round(m,2))
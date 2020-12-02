#Python Program to Find the Sum of Sine Series
import math
def sin(x,n):
    sine=0
    pi=22/7
    r=(pi/180)*x
    for i in range(n):
        sign=(-1)**i
        sine=sine+((r**(i*2.0+1))/math.factorial(i*2.0+1))*sign
    return sine

x=int(input("Enter degree of sin:"))
n=int(input("Enter number of term:"))
print("Result=",round(sin(x,n),2))
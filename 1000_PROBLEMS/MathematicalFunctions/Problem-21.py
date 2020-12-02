#Python Program to Find the Area of a Triangle Given All Three Sides
import math
a=int(input("Enter 1st side:"))
b=int(input("Enter 2nd side:"))
c=int(input("Enter 3rd side:"))

s=(a+b+c)/2

Area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is :",round(Area,3))
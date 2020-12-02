#Python Program to Create a Class and Compute the Area and the Perimeter of the Circle
import math
class Area_Of_Rectangle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        return math.pi*self.radius*self.radius
    def Perimeter(self):
        return 2*math.pi*self.radius
    def display(self):
        print("The Area is:",round(s.Area(),2))
        print("The Perimeter is:",round(s.Perimeter(),2))

n=int(input("Enter radius of the circle:"))
s=Area_Of_Rectangle(n)
s.display()



"""
class Area_Of_Circle:
    def __init__(self):
        self.radius=r

    def cal(self,r):
        pi=3.1416
        n =pi*self.radius*self.radius
        m= 2*pi*self.radius

        print("The Area is:",round(n,2))
        print("Perimeter of the Circle:",round(m,2))
r=int(input("Enter radious of circle:"))
k=Area_Of_Circle()
k.cal(r)
"""




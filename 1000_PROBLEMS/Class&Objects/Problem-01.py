#Python Program to Find the Area of a Rectangle Using Classes
class Area_Of_Rectangle:
    def __init__(self,Base,Height):
        self.Base=Base
        self.Height=Height
    def calculate(self):
        return self.Height*self.Base

m=int(input("Enter Base:"))
n=int(input("Enter height:"))
p=Area_Of_Rectangle(m,n)
print("The Area is:",p.calculate())
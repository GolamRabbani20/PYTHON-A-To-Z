class rectangle:


   def __init__(self,hight,base): #constractor
       self.hight=hight
       self.base=base


   def area_calculate(self):     #Function/Method
       area=0.5*self.hight*self.base
       print("Area=",area)

h=int(input("Enter hight:"))
b=int(input("Enter Base:"))
x=rectangle(h,b)   #Object
x.area_calculate()
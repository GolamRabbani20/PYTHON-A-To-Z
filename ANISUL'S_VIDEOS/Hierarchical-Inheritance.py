# Class_A <--- Class_B & Class_C

class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def area(self):
        print("I am happy")


class trangal(shape):
    def area(self):
        a=.5*self.x*self.y
        print("Area=",a)

class rectangle(shape):
    def area(self):
        r=self.x*self.y
        print("Area=",r)


result=trangal(10,20)
r=rectangle(10,20)
result.area()
r.area()

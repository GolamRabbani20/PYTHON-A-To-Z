class shape:
    def __init__(self,d1,d2):
        self.dim1=d1
        self.dim2=d2

    def area(self):
        #print("Hello")
        pass

class rectangle(shape):
        def area(self):
          a=self.dim1*self.dim2
          print("Area of Rectangle:",a)


class tringel(shape):
    def area(self):
        x=0.5*self.dim1*self.dim2
        print("Area of Triangle:",x)


k=rectangle(10,20)
k.area()

p=tringel(20,30)
p.area()
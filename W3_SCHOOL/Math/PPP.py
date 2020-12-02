class rectangle:
    #height=""
    #wide=""
    def __init__(self,h,w):
        self.height=h
        self.wide=w
    def dis(self):
        #result=self.height*self.wide
        #print(result)
        return self.height*self.wide

h=int(input("Enter height:"))
w=int(input("Enter wide:"))
s1=rectangle(h,w)
print("Area of rectangle:",s1.dis())
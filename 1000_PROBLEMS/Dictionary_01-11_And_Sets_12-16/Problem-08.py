#Python Program to Form a Dictionary from an Object of a Class
class A(object):
    def __init__(self,m,n):
        self.A=m
        self.B=n
obj=A(101,'Ranna')
print(obj.__dict__)
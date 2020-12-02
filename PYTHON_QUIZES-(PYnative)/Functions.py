"""
print('%x,%X' % (15,15))

def OuterFun(a,b):
    def innerFun(c,d):
        return c+d

    return innerFun(a,b)
res=OuterFun(5,10)
print(res)

#/////////

def x(name,age=20):
   print(name,age)
x('Emma',25)

def x(a,b):
    def y(c,d):
        return c+d
    return y(a,b)
    return a
r=x(5,10)
print(r)

def x(**a):
    print(a)
    for i in a:
        print(i)
x(id=256,name="Ranna",salary=2563)

def add(a,b):
    return a+5,b+10
p=add(10,20)
print(p)

def x(a):
    return a+10
x(10)
print(a)
"""
def )
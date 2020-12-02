
x,y=10,20
n=x+y  #30

def m():
    global n
    n=100
    print("Changed=",n)

def b():
    n=5+6
    print("Result=",n*2)

def f():

    print("Golbal=",n*10)

m()
b()
f()


def add(x,y):
    print("Sum=",x+y)

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
add(a,b)
def sub(p,q):
    subt=p-q
    return subt
print("Subtraction=",sub(a,b))

def div(m,n):
    d=m/n
    return d
print(div(56,9))

def large(a,b):
    if a>b:
        return a
    else:
        return b

result=large(250,23)
print("Result=",result)
x=0
def lcm(a, b):
    global x
    x = x + b
    if ((x % a == 0) and (x% b == 0)):
        return x
    else:
        lcm(a, b)
    return x

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if a > b:
    LCM = lcm(b, a)
else:
    LCM = lcm(a, b)
print(LCM)

'''
def lcm(a,b):
    lcm.multiple=lcm.multiple+b
    print(lcm.multiple)
    if((lcm.multiple % a == 0) and (lcm.multiple % b == 0)):
        return lcm.multiple;
    else:
        lcm(a, b)
    return lcm.multiple
lcm.multiple=0  # it works as a global variable
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if(a>b):
    LCM=lcm(b,a)
else:
    LCM=lcm(a,b)
print(LCM)
'''
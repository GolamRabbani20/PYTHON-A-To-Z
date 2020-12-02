from functools import reduce
num=[2,3,5,6,7,8]

double=list(map(lambda k:k*2,num))
print(double)

def Add_all(a,b):  #For this purpose this function always accept two parameters
    return a+b
SumOFDouble=reduce(Add_all,double)
print(SumOFDouble)

Sum=reduce(lambda a,b:a+b,num) #2+3+5+6+7+8
print(Sum)
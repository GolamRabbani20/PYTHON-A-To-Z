from functools import reduce
num=[5,6,12,20,45,125]
def LCM(n1,n2):
    Max=max(n1,n2)
    while(True):
        if Max%n1==0 and Max%n2==0:
            return Max
        else:
            Max+=1

Result=reduce(LCM,num)
print(Result)
from functools import reduce
def LCD_List(a):
    return reduce(LCD,a)

def LCD(x,y):
    return x*y//(GCD(x,y))

def GCD_List(b):
    return reduce(GCD,b)

def GCD(x,y):
    while x%y!=0:
        x,y=y,(x%y)
    return y

def main():
    m,n=input().split()
    m,n=[int(m),int(n)]
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    LCD_value=LCD_List(a)
    GCD_value=GCD_List(b)

    x=LCD_value
    count=0

    while x<=GCD_value:
        if GCD_value%x==0:
            count+=1
        x+=LCD_value
    print(count)

if __name__=="__main__":
    main()
def FindDigits(n):
    x=[]
    while n>=1:
        r=n%10
        x.append(r)
        n=n//10
    return x

t=int(input())
while t:
    n=int(input())
    count=0
    for i in FindDigits(n):
        if i>0 and n%i==0:
            count+=1
    print(count)
    t-=1


def CountN(x,n):
    pos=0
    neg=0
    zero=0
    for k in x:
        if k>0:
            pos+=1
        elif k<0:
            neg+=1
        else:
            zero+=1

    print(format(pos/n,".6f"))
    print(format(neg/n,".6f"))
    print(format(zero/n,".6f"))

x = []
n=int(input())
m=input().split()
for i in m:
    x.append(int(i))

CountN(x,n)

def KaprekarNumbers(p,q):
    lst=[]
    for i in range(p,q+1):
        if i>3:
            d=len(str(i))
            k=len(str(i**2))
            x=str(i*i)

            r=int(x[k-d:k+1])
            l=int(x[:k-d])

            if (l+r)==i:
                lst.append(i)

        elif i==1 or i==0:
            lst.append(i)

    return lst,len(lst)

p=int(input())
q=int(input())
n,m=KaprekarNumbers(p,q)
if m:
    for k in n:
        print(k,end=" ")
else:
    print("INVALID RANGE")

def SubArrayDivision(x,d,m):
    count=0
    n=(len(x)-m)+1
    for i in range(n):
        if sum(x[i:i+m])==d:
            count+=1
    return count

input()
x=list(map(int,input().split()))
d,m=input().split()
d,m=[int(d),int(m)]
print(SubArrayDivision(x,d,m))
def BeautifulTriplets(x,d):
    count=0
    for i in x:
        if x.count(i+d):
            if x.count(i+d*2):
                count+=1
    return count

n,d=input().split()
d=int(d)
x=list(map(int,input().split()))
print(BeautifulTriplets(x,d))

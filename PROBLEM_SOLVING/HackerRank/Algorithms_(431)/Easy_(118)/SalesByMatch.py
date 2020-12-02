def SaleByMatch(x,r_item):
    k=[0]*101
    for i in x:
        k[i]+=1
    return list(filter((r_item).__ne__,k))
input()
x=list(map(int,input().strip().split()))
count=0
for j in SaleByMatch(x,0):
    count+=j//2
print(count)
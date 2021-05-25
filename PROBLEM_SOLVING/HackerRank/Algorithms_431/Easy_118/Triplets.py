a=[]
b=[]
a_point=0
b_point=0

for i in input().split():
    a.append(int(i))
for k in input().split():
    b.append(int(k))
for p in range(len(a)):
    if a[p]>b[p]:
        a_point+=1
    elif a[p]<b[p]:
        b_point+=1

print(a_point,b_point)



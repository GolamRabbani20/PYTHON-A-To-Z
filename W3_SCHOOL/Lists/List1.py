x=[]
k=input().split()
h=0
for i in k:
    x.insert(h,int(i))
    h+=1
x.insert(10,58)
new=[2,2,5,63,5,585]
print(x+new)
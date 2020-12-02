n,h=input().split()
height=input().split()
c=0
for k in height:
    if int(k)>int(h):
        c+=2
    else:
        c+=1
print(c)

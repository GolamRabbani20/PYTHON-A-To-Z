n=int(input())
a=input()
Level=0
Valleys=0
for k in a:
    if k=='U':
        Level+=1
        if Level==0:
            Valleys+=1
    else:
        Level-=1
print(Valleys)
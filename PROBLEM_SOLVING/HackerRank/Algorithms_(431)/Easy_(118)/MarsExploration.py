s=input()
s1='SOS'*(len(s)//3)
count=0
i=0
for k in s:
    if s1[i]!=k:
        count+=1
    i+=1
print(count)
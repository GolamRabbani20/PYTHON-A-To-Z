def StrongPassword(n,pw):
    count=0
    if any(i.isdigit() for i in pw)==False:
         count+=1
    if any(i.islower() for i in pw)==False:
         count+=1
    if any(i.isupper() for i in pw)==False:
        count+=1
    if any(i in '!@#$%^&*()-+' for i in pw)==False:
        count+=1
    return max(count,6-n)

n=int(input())
x=input()
pw=[]
for i in range(n):
    pw.append(x[i])
print(StrongPassword(n,pw))
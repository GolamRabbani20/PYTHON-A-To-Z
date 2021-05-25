s=input()
n=int(input())
ln=len(s)
count=s.count('a')*(n//ln)
p=n%ln                           #n-ln*(n//ln)
for i in range(p):
    if s[i]=='a':
        count+=1
print(count)
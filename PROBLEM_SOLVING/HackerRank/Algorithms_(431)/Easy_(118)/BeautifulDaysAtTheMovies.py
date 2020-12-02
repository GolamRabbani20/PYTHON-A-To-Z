S,E,k=input().split()
count=0
for i in range(int(S),int(E)+1):
    n=i
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if abs(rev-i)%int(k)==0:
        count+=1
print(count)
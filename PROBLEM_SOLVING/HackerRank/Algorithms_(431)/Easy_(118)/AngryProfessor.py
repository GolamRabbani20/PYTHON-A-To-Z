def AngryProfessor(st,k):
    count=0
    for i in st:
      if i<=0:
          count+=1
    if count>=k:
        return False
    else:
        return True

t=int(input())
x=[]
while t:
    n,k=map(int,input().strip().split())
    st=list(map(int,input().strip().split()))
    x.append(AngryProfessor(st,k))
    t-=1
for i in x:
    if i:
        print("YES")
    else:
        print("NO")

def SaveThePrisoner(n,m,s):
    return (m+s-2)%n+1

t=int(input())
while t:
    n,m,s=input().strip().split()
    n,m,s=[int(n),int(m),int(s)]
    print(SaveThePrisoner(n,m,s))
    t-=1

def Gemstones(x):
   p=set(x[0])
   for k in x[1:]:
       p=p.intersection(set(k))
   return len(p)

n=int(input())
x=[]
while n:
    x.append(input())
    n-=1
print(Gemstones(x))

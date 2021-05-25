def MinSum(p):
   sum=0
   for i in range(4):
       sum+=min(p)
       x.remove(min(p))
   return sum

def MaxSum(x):
   sum1=0
   for j in range(4):
       sum1+=max(x)
       x.remove(max(x))
   return sum1

x=[]
for k in input().split():
    x.append(int(k))
p=x.copy()
print(MinSum(x),MaxSum(p))
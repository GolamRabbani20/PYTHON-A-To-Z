'''def Smart_Number(n):
    count=0
    for k in range(1,n+1):
        if n%k==0:
            count+=1
    return count
x=[]
for i in range(int(input())):
    x.append(Smart_Number(int(input())))
for s in x:
    if s%2==1:
        print("YES")
    else:
        print("NO")'''

import math
def is_smart_number(num):
    val = int(math.sqrt(num))
    if num-val*val==0:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")






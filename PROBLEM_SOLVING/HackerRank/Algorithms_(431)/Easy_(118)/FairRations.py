"""def FairRation(B):
    B = [i for i, element in enumerate(B) if element%2]
    #print(B)
    if len(B)%2:
        return "NO"
    counter = 0
    for i in range(0,len(B),2):
        counter+=(B[i+1]-B[i])*2
    return counter

input()
B=list(map(int,input().strip().split()))
print(FairRation(B))"""

def FairRation(B,n):
    A=[]
    for i in range(n):
        if B[i]%2:
            A.append(i)
    if len(A)%2:
        return "NO"
    count=0
    for k in range(0,len(A),2):
        count+=(A[k+1]-A[k])*2
    return count

n=int(input())
B=list(map(int,input().strip().split()))
print(FairRation(B,n))

x=[2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n=len(x)
k=max(x)
count=[0,0,0,0,0,0,0,0,0,0]
print("The unsorted list is:",x)
for j in range(n):
    count[x[j]]+=1
print("Frequency counting list:",count)
for i in range(1,k+1):
    count[i]=count[i]+count[i-1]
print("Updated frequency counting list:",count)
for p in range(n-1,-1,-1):
    count[x[p]]-=1
    b[count[x[p]]]=x[p]
for l in range(n):
    x[l]=b[l]
del b
print("The final sorted list is:",x)
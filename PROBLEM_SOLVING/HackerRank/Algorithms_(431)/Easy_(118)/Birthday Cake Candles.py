def BirthdayCakeCandles(x):
    count=0
    Max=max(x)
    for i in x:
        if i==Max:
            count+=1
    return count

n=int(input())
x=[]
for k in input().split():
    x.append(int(k))
print(BirthdayCakeCandles(x))
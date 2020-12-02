def Bill_Division(k,Bill,b):
    if (sum(Bill)-Bill[k])//2==b:
        return 1
    else:
        return b-(sum(Bill)-Bill[k])//2   #Or return Bill[k]//2

n,k=input().strip().split()
k=int(k)
Bill=[i for i in map(int,input().strip().split())]
b=int(input())
if Bill_Division(k,Bill,b)==1:
    print("Bon Appetit")
else:
    print(Bill_Division(k,Bill,b))
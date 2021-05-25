def FunnyString(x):
    for i in range(len(x)//2):
        if abs(ord(x[i])-ord(x[i+1]))!=abs(ord(x[-i-1])-ord(x[-i-2])):
            print("Not Funny")
            break
    else:
        print("Funny")

t=int(input())
while t:
    FunnyString(input())
    t-=1

'''def FunnyString(x):
    x1=list(reversed(x))
    for i in range(len(x)-1):
        if abs(ord(x[i])-ord(x[i+1]))!=abs(ord(x1[i])-ord(x1[i+1])):
            print("Not Funny")
            break
    else:
        print("Funny")

t=int(input())
while t:
    FunnyString(input())
    t-=1'''
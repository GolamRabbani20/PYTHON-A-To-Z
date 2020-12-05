def SherlockAndSquares(a,b):
    count=0
    x=1
    while x*x<a:
        x+=1
    while x*x<=b:
        count+=1
        x+=1
    return count

t=int(input())
while t:
    a,b=input().strip().split()
    a,b=[int(a),int(b)]
    print(SherlockAndSquares(a,b))
    t-=1
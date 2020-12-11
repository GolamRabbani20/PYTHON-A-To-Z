def ExtraLongFactorials(n):
    if n==1:
        return 1
    return n*ExtraLongFactorials(n-1)

n=int(input())
print(ExtraLongFactorials(n))


"""
print("Using Loop=",Using_Loop(m))
def Using_Loop(m):
    s=1
    for i in range(m,0,-1):
        s*=i
    return s
"""



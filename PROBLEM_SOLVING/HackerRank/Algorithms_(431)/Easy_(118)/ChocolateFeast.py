def ChocolateFeast(bars,m):
    wp = bars
    while wp >= m:
        bars += wp//m
        wp = wp//m + wp%m
    return bars

for i in range(int(input())):
    n,c,m = map(int,input().split())
    print(ChocolateFeast(n//c,m))

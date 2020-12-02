c=p=0
for i in range(int(input())):
    magnet=int(input()) #input()
    c += magnet!=p
    p=magnet
print(c)
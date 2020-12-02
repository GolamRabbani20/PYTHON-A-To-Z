from math import floor
L=floor(5/2)
C=L
for i in range(1,int(input())):
    L=floor(L*3/2)
    C+=L
print(C)
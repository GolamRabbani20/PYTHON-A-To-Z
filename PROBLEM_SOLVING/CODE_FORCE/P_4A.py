"""w=int(input())
if w==2 or w%2==1:
    print("NO")
else:
    print("YES")
"""

w=2**int(input())%24
print("YNEOS"[w<9::2])  #if w<9 is true that means 1:5(Length of string):2
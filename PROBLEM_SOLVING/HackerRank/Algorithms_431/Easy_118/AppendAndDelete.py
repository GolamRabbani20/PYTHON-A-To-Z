s = input().strip()
t = input().strip()
k = int(input().strip())
for m in reversed(range(1,k+1)):
    if s==t[:len(s)] and len(t)-len(s)==m or len(s)==0:
        break
    s=s[:-1]
print ("Yes" if abs(len(t)-len(s))<= m else "No")
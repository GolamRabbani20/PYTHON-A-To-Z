x=list(map(int,input().strip().split()))
word=input()
m=[]
for k in range(len(word)):
    m.append(x[ord(word[k])-97])
print(len(word)*max(m))
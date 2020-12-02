print("Solution-1")
k={'0'}
k.update(input().split())
print(4-len(k)+1)

print("Solution-2")
m={*input().split()}
print(4-len(m))

print("Solution-3")
print(4-len({*input().split()})) # here * deowha mane sob gula k akshte set a add kora

print("Solution-4")
s={'0'}
k=input().split()
for m in k:
    s.update(m)
print(4-len(s)+1)
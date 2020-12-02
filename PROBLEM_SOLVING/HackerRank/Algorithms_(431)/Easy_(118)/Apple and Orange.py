s,t=input().split()
s=int(s)
t=int(t)

a,o=input().split()
a=int(a)
o=int(o)

m,n=input().split()

apple=input().split()
orange=input().split()
apples=0
oranges=0

for k in apple:
    if int(k)+a>=s and int(k)+a<=t:
        apples+=1

for i in orange:
    if int(i)+o>=s and int(i)+o<=t:
        oranges+=1

print(apples)
print(oranges)


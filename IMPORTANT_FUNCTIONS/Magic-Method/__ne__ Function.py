#__ne__ is used for removing same kind of occurence in the list
#ne= not equal
x=[1,2,0,0,5,5,5,5,3,6,0,0,0,0,0,0]
k=5
p=0
m=list(filter(k.__ne__,x))
n=list(filter(p.__ne__,m))

print(m)
print(n)

y=[-2,20,5,-6,-10,-47,120]
t=list(filter(k.__neg__,y))
print(t)
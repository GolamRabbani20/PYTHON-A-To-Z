x=("Rabbani","Hemel","Habib")
y=(1,2,3)
z=list(zip(y,x))
d=set(zip(y,x))
e=dict(zip(y,x))
t=tuple(zip(y,x))
print(z)
print(d)
print(e)
print(t)

for a,b in zip(y,x):
    print(a,b)

for i in t:
    print(i)
print()

for k  in e:
    print(k)
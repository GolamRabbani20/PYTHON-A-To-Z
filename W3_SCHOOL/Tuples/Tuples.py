"""
d= "lata", 250 ,250,"Love"
r,s,t,u=d
print(t)
print(d)

x=("Klala","Apple",25,69,45,"Book")
print(len(x))
if "Apple" is x:
    print("Yes")

print(x)
print(x[:5])

m=list(x)
m[3]="Lazina"
x=tuple(m)
print(x)

k=("hkla","jilo",145,123,369,56)

b=x+k
print(b)

for m in x:
    print(m)

t=tuple(("ljh","koit","hjyu",526.78,456,120,120,120,36,36))
print("T=",t[2:5])

print(t.count(120))
print(t.index(36))
print(t.index(120))

#fat=(1205,'a')
#print(max(fat))

aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
j=aTuple[1][1]

print(j)

"""
x=(2,5,6,8,9,20,26,45,36)
#x.pop(2)
print(x*2)

a=("stringlok",)
print(type(a))
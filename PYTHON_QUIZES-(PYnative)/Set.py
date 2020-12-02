a={"Orange","Red","white",'solow'}
b={"Yellow","Red","Red","Blue","Black","white"}
a.update(["Blue", "Green", "Red"])
print(a)
a.pop()
a.discard("Orange")

print(a)
print(b)
#d=set(a)
#print(d)

#b.difference_update(a)
#print(b)



#c=b.copy()
#print(c)

x={5,2,20,10,30}
y={50,60,"20",70,100,30,2}
y.discard("201")
print(y)
z=x.union(y)
print(z)

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}
se=set2.difference(set1)
print(se)
print(set1.issubset(set2))
print(set2.issubset(set1))

aSet = {1, 'PYnative', ('abc', 'xyz'), True}
print(aSet)
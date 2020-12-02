x={7,2,3,87,6,36,5,56}
y=set([3,7,87,12,10,0,4])

x.add(102)
y.add(120)
x.remove(36)
print(7 in y) #checking 7 element
print(11 not in x)
print(x)
print(y)
print("Union=",x|y) #x,y sets Union
print("Intersection=",x&y) #x,y sets intersection
print("Difference",y-x) #difference

lst=[4,5,52,5,66,7,8,9,50]
double=list(map(lambda k:k*2,lst)) #map(function,iterable)
for i in double:
    print(i,end=" ")
print()

def Update(k):
    return k**3
double2=map(Update,lst)
for p in double2:
    print(p,end=" ")
print()

s1=[2,5,8,10]
s2=[4,5,9,12]
lst1=map(lambda x,y:x+y,s1,s2)
for k in lst1:
    print(k,end=" ")
print()

test=['pen','Apple','python']
r=list(map(list,test))
print(r)
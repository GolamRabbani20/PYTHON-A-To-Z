x=["Python",[5,6,25,12,20,],['d','b',7,5]]
print(x[0][2])
print(x[1][3])
print(x[2][3])

m=[50,6,6,9,71,89,68,56]
n=["abba","ammaha","alu","egg"]
#print(m+n)

m[1:4]=[2,5,8,96,3,20,45]
print(m)

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

s=[5,7,0,63,25,45]
v=[2*x for x in s]
print(v)
#c=s.copy()

print(s[::-2])

a=["Golam","Rabbani"]
print("-".join(a))

l=[None]*10
print(len(l))

list2 = [4, 8, 12, 16,20]
print(list2[-4:-1])
list2.append(16)
print(list2)

del list2[0:60]
print(list2)

f=["Python","Love","lkinjtyrou"]
print(max(f))

g=[x+y for x in ["Hello","Good"] for y in ["Dear","Bye"]]
print(g)

q=[4,52,10,63]
a1=[1,2,3]
new1=list(q) #copying a list
new=q.extend(a1)
print(new1)

list1 = ['xyz', 'zara', 'PYnative']
print (max(list1))
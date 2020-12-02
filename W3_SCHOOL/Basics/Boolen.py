x=10
y=12

print(x is not y)
y+=10
print(y)
print(x<y)
print(bool("Hello"))
print(bool(15))

print(isinstance(x,int))

p=bool(["apple","pinaple","lala"])
print(p)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
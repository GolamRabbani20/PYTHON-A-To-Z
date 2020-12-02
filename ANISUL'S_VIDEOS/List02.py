y=["Computer",20,"Keyboard","CPU","Phone"]

pos=y.index("CPU")
print("Position=",pos)

print("\nLength=",len(y))
y.append("Rabbani,Ashulia,2016,25.20")
print(y)
print("\nLength=",len(y))

y.insert(3,"Anisul,01761793058")
print(y)

y.remove(20)
y.remove("CPU")

print(y)
y.sort()
print(y)

p=[20,45,10,10,10,8,963,10,10,15,4587,52,8,8,8,36,54,8,8]

print("Position=",p.index(52))
print("Count=",p.count(10))


a=p.copy()
print("\nList a=",a)

p.sort()
print("\n",p)
p.reverse()
print(p)
p.pop()
p.pop()
print(p)

p.clear()
print("All data have been cleared",p)

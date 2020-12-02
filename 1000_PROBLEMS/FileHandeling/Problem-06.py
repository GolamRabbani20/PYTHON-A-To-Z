#Python Program to Copy the Contents of One File into Another
x=open("data101.txt")

m=open("data102.txt","w")
for k in x:
    m.write(k)
m=open("data102.txt",'r')
print(m.read())
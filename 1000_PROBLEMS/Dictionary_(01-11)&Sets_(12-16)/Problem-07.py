#Python Program to Remove the Given Key from a Dictionary
'''
p={'a':20,'b':30,'c':50,'d':100}
n=input("Enter key:")
if n in p:
   del p[n]

else:
    print("The key is not found")
    exit(0)
print(p)
'''
n=int(input("Enter size:"))
d={}
t=n
for i in range(n):
    k=int(input("Enter int as key"+str(i+1)+":"))
    v=input("Enter a sting:")
    d.update({k:v})
print("Initial dic:",d)

for t in range(n):
    w=int(input("Enter a key:"))
    if w in d:
        del d[w]
        print(d)
    else:
      print("The key is not found!")
      #exit(0)


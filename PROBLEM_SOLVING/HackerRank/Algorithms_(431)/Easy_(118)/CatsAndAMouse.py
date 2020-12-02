def CatsAndAMouse(x,y,z):
    x=int(x)
    y=int(y)
    z=int(z)
    if abs(z-x)<abs(z-y):
        return 1
    elif abs(z-x)>abs(z-y):
        return 2
    else:
        return 0

s=[]
for k in range(int(input())):
   x,y,z=input().split()
   s.append(CatsAndAMouse(x,y,z))

for r in s:
    if r==1:
        print("Cat A")
    elif r==2:
        print("Cat B")
    else:
        print("Mouse C")


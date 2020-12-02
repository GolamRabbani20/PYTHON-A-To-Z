#Python Program to Print all Numbers in a Range Divisible by a Given Number
x=int(input("Enter a lower range:"))
y=int(input("Enter a upper range:"))
v=int(input("Enter divisiable number:"))
for i in range(x,y):
    if i%v==0:
      print(i)
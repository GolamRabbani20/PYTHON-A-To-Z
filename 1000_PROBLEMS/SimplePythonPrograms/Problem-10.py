#Python Program to Print Odd Numbers Within a Given Range
x=int(input("Lower range:"))
y=int(input("Upper range:"))

for i in range(x,y):
     if i%2==1:
         print(i)

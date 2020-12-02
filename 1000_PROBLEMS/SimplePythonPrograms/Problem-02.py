#Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
x=int(input("Enter 1st value:"))
y=int(input("Enter 2nd value:"))

x=x+y
y=x-y
x=x-y

print("X=",x)
print("Y=",y)
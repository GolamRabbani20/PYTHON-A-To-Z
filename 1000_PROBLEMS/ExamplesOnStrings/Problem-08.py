#Python Program to Remove the Characters of Odd Index Values in a String
x=input("Enter a string:")
for i in range(len(x)):
    if i%2==0:
        print(x[i],end="")

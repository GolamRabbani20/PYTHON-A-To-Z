#Python Program to Form a New String where the First Character and the Last Character have been Exchanged
x=input("Enter a string:")
#print(x[len(x)-1]+x[1:len(x)-1]+x[0])
m=x[-1]+x[1:-1]+x[0]
print(m)
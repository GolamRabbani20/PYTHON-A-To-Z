#Python Program to Compute Simple Interest Given all the Required Values
a=int(input("Enter amount:"))
t=int(input("Enter time in(Year):"))
r=float(input("Enter rate:"))

interest=(a*t*r)/100
print("Interest is :",interest)
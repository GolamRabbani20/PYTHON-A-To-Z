#Python Program to Accept Three Digits and Print all Possible Combinations from the Digits
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

x=[]
x.append(a)
x.append(b)
x.append(c)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i!=j & j!=k & k!=i):
                print(x[i],x[j],x[k])

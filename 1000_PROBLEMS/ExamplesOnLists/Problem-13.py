#Python Program to Generate Random Numbers from 1 to 20 and Append Them to the Lis
import random
n=int(input("Enter number of elements:"))
x=[]
for k in range(n):
    x.append(random.randint(1,20))
print("Random number list:",x)
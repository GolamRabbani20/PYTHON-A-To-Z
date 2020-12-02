#Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
m=input("Enter 1st string:")
n=input("Enter 2nd string:")
k=0
p=0
for i in m:
   k+=1
for j in n:
    p+=1
    
if k>p:
    print("The Longer String is:", m)
elif p==k:
    print("Both string are equal")
else:
    print("The Longer String is:", n)

'''
if len(m)>len(n):
    print("The Longer String is:",m)
else:
    print("The Longer String is:", n)
'''
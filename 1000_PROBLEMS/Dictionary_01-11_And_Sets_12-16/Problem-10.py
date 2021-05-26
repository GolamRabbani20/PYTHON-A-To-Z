#Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
s=input("Enter a string:")
#x=[k for k in s.split()]
x=[]
x=s.split()

z=[x.count(p) for p in x]

print(set(zip(x,z)))


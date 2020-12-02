#Python Program to Read the Contents of a File in Reverse Order
s=input("Enter file name:")
#x=open(s,"r")
#print(x.readlines()[::-1],end=" ")
for line in reversed(list(open(s))):
    print(line.rstrip())
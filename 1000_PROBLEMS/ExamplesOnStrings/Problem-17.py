#Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String
x=input("Enter a string:")
p=x[0:2]+x[-2:]
print("The new string: "+p)
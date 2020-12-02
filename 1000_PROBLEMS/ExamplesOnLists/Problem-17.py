#Python Program to Read a List of Words and Return the Length of the Longest One
n=int(input("Enter number of elements:"))
x=[]
for i in range(n):
    x.append(input("Enter element of word:"))

max1=len(x[0])
temp=x[0]

for k in x:
    if len(k)>max1:
        max1=len(k)
        temp=k
print("The word with the longest length is:",temp)



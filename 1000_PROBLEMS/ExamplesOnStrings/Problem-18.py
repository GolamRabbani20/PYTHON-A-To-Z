#Python Program to Count the Occurrences of Each Word in a Given String Sentence
s=input("Enter a sentence:")
x=input("Enter search string:")

m=[m for m in s.split()]
c=0
for i in m:
    if i==x:
        c+=1
print("The number of word:",c)
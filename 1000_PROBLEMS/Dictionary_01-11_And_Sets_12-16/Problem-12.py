#Python Program to Count the Number of Vowels Present in a String using Sets
x=input("Enter a string:")
c=0
s=set("aeiouAEIOU")
for i in x:
    if i in s:
        c+=1
print("Total vowels:",c)
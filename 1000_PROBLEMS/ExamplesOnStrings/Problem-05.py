#Python Program to Count the Number of Vowels in a String
s=input("Enter a string:")
C=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' :
        C+=1
print("Number of vowels:",C)
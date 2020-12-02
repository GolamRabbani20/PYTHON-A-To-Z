#Python Program to Calculate the Number of Words and the Number of Characters Present in a String
s=input("Enter a string:")
word=0
ch=0
for i in s:
    if i==" ":
        word+=1
    else:
        ch+=1
print("Number of words=",word+1)
print("Number of characters=",ch+word)
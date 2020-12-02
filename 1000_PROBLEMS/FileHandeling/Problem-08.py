#Python Program to Read a Text File and Print all the Numbers Present in the Text File
x=open("data12.txt","r")
c=0
for line in x:               #text file TO single line
    words=line.split()       #Sngle line TO list of words
    for word in words:       #List of word TO single word
        for letter in word:  #Single word TO letter
           #if letter<='9' and letter>='0':
            if letter.isdigit():
               print(letter,end=" ")
               c=c+1
print("\nTotal numbers=",c)
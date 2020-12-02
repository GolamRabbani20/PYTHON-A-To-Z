#Python Program that Reads a Text File and Counts the Number of Times a Certain Letter Appears in the Text File
x=open("data101.txt","r")
n=input("Enter a letter:")
c=0
for line in x:               #text file TO single line
    words=line.split()       #Sngle line TO list of words
    for word in words:       #List of word TO single word
        for letter in word:  #Single word TO letter
           if letter==n:     #Checking
              c=c+1          #Counting

print(c)
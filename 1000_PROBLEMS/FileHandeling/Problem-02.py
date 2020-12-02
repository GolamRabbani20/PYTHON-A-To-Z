#Python Program to Count the Number of Words in a Text File
s=input("Enter file name:")
n=0
#with open(s,"r") as x:
x=open(s,"r")
for k in x:         #x thake 1 ta kore line k te dibe
    #print(k)
    words=k.split()
    n=n+len(words)
print(n)




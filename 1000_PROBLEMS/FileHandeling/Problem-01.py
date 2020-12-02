#Python Program to Read the Contents of a File
a=input("Enter the name of the file with .txt extension:")
s=input("Enter mode:")
file2=open(a,s)
for i in range(5):
   x=input("Enter input:")
   file2.write(x)
   file2.write("\n")

file2=open(a,"r")
line=file2.readline()
while(line!=""):
    print(line,end="")
    line=file2.readline()
file2.close()
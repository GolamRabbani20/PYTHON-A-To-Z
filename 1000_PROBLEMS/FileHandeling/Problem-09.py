#Python Program to Append the Contents of One File to Another File
s=input("Enter file to be read from:")
x=open(s,'r')
data=x.read()
x.close()

s1=input("Enter file to be appended to:")
a=open(s1,'a')
a.write(data)
a=open(s1,'r')
print("After appending the file:",a.read())
a.close()
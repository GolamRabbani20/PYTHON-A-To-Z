m=open("My-details.text","r") #r=read kora w=write kora & r+ = read & write
#print(m.readable()) #Check the file is  readabe or not
#print(m.writable()) #Check the file is writable or not

text=m.read()
#text=m.readlines()#sobgula k akta file a convert korbe
#text=m.readlines() [2] # it will print 3 no line of the file
#text=m.readline() #it will print first line only of the file
'''
for x in m: # Uning loop
     print(x)
'''
print(text)
#print("No of Characters:",len(text)) #Koto gulo characters ase se gulo count korbe
m.close()
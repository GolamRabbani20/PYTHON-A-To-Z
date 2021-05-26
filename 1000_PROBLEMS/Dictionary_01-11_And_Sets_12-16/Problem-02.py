#Python Program to Concatenate Two Dictionaries Into One
d1={1:"I",2:"Love",3:"You"}
d2={4:"Very",5:"much",6:"Lazina"}
d1.update(d2)
print("Updated:",d1)

x1={}
for i in range(2):
    k=int(input("Enter key:"))
    v=input("Enter a string:")
    x1.update({k:v})

x2={}
for i in range(2):
    k=int(input("Enter key:"))
    v=input("Enter a string:")
    x2.update({k:v})

x1.update(x2)
print(x1)
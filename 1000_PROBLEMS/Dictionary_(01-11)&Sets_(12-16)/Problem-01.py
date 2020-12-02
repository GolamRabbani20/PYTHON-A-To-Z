#Python Program to Add a Key-Value Pair to the Dictionary
dis={}
for i in range(3):
    k = int(input("Enter a key:"))
    v = int(input("Enter a value:"))
    dis.update({k:v})
print("The update dictionary is:",dis)
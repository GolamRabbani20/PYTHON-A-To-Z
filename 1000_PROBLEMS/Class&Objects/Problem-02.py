#Python Program to Append, Delete and Display Elements of a List Using Classes
class ramadan:
    def __init__(self):
        self.lst=[]
    def add(self,a):
        return self.lst.append(a)
    def remove(self,a):
        return self.lst.remove(a)
    def dis(self):
        return self.lst

obj=ramadan()

n=1
while n!=0:
    print("Press 1 for append:")
    print("Press 2 for delete:")
    print("Press 3 for Display:")
    print("Press 0 for Exit:")
    n=int(input("Chose your option:"))
    print("\n")

    if n==1:
        x=int(input("Enter a value:"))
        obj.add(x)
        print("Result is:",obj.dis())

    elif n==2:
         y=int(input("Enter a value:"))
         obj.remove(y)
         print("The Update list:",obj.dis())

    elif n==3:
        print("The list is:",obj.dis())

    elif n==0:
        exit(0)
    else:
        print("Invalid!")
    print()
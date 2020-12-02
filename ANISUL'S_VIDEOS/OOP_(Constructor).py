class teacher:
    name=""
    id=""
    age=""

    def __init__(self,name,id,age): #it is a constractor
        self.name=name
        self.id=id
        self.age=age

    def dispaly(self):
        print(f"\nName:{m.name}\nID:{m.id}\nAge:{m.age}")

for i in range(int(input("Enter value of n:"))):
     n=input("Enter a name:")
     id=input("Enter your ID:")
     age=input("Enter your Age:")

     m=teacher(n,id,age)  #object where we have passed the value for constractor
     m.dispaly()

     print("\n")

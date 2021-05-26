class student:
    roll=""
    name=""
    gpa=""

    def display(self):
        print("\t")
        print(f"Name={self.name}\nRoll={self.roll}\nGPA={self.gpa}")

    def setValue(self,name,roll,gpa):
        self.name=name
        self.roll=roll
        self.gpa=gpa

x = student()

for i in range(int(input("Enter n:"))):
     #x = student()
     n=input("Enter your name:")
     r=input("Enter roll name:")
     g=input("Enter GPA name:")

     x.setValue(n,r,g)
     x.display()

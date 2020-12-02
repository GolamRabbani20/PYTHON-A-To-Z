#Python Program to Create a Class which Performs Basic Calculator Operations
class calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        return self.x/self.y

x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
k = calculator(x,y)
print("\n")
n=1
while n!=0:

    print("1.Add.")
    print("2.Subtraction.")
    print("3.Multiplication.")
    print("4.Division.")
    print("0.Exit.")
    n=int(input("Chose a option:"))
    print()
    if n==1:
        print("Sum is:",k.add())
        print()
    elif n==2:
        print("The subtraction is:",k.sub())
        print()
    elif n==3:
        print("The multiplication is:",k.mul())
        print()
    elif n==4:
        print("The division is:",k.div())
        print()
    elif n==0:
        exit(0)
    else:
        print("Invalid Chose!")
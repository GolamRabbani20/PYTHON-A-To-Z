class Stack:
    def __init__(self):
        self.Array=[]
        self.top=-1

    def push(self):
        item=input("Enter item:")
        self.top += 1
        self.Array.append(item)


    def Pop(self):
        x=0
        if self.top==-1:
            print("Stack underflow!")
        else:
           x=self.Array.pop()
           self.top-=1
        return x

    def Peekdata(self):
        if self.top==-1:
            print("Empty!")
        else:
            print("Top data of the stack:",self.Array[self.top])

    def display(self):
        print("Stack data:")
        if self.top==-1:
            print("Stack is empty!")
        else:
            for k in reversed(self.Array):
                print(k)

lst=Stack()
while True:
    n = input("Do you want to Push?(Y/N):")
    if n.upper() == 'Y':
        lst.push()
    elif n.upper() == "N":
        lst.display()
        break
while True:
    n=input("Do you want to pop?(Y/N):")
    if n.upper()=='Y':
        print("After popped {}:".format(lst.Pop()))
        lst.display()

    elif n.upper()=="N":
        break

lst.Peekdata()


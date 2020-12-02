#Implementation of Stack Using Array....By Static Memory Allocation
class Stack:
    def __init__(self,size):
        self.Stack=[]
        self.size=size
        self.top=-1 #Top is a pointer

    def push(self,item):
        if len(self.Stack)==self.size:
            print("Stack overflow!")

        else:
            self.top+=1
            self.Stack.append(item)

    def Pop(self):
        result=0
        if self.top==-1:
            print("Underflow!")
        else:
            result=self.Stack.pop()
        return result

    def Check_Stack_Full_Or_Not(self):
        if len(self.Stack)==self.size:
            print("The stack is full.")
        else:
            print("The is not full.")


    def display(self):
        print("Stack data:")
        temp=-1
        if self.Stack==[]:
            print("The stack is empty!")
        else:
            for k in reversed(self.Stack):
                print(k)

lst=Stack(int(input("Enter size:")))
data=input("Enter data:").split()
for i in data:
    lst.push(i)

lst.display()
lst.Pop()
lst.display()
lst.Check_Stack_Full_Or_Not()
lst.push(200)
lst.display()
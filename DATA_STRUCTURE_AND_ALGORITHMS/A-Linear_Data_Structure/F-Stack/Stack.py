#Implementation of Stack Using Array....By Static Memory Allocation
class Stack:
    def __init__(self,size):
        self.Stack=[]
        self.Size=size

    def Push(self,item):
        if len(self.Stack)==self.Size:
            print("The stack is full!")

        else:
            self.Stack.append(item)

    def POP(self):
        result=-1
        if self.Stack==[]:
            print("The stack is empty!")
        else:
            result=self.Stack.pop()

        return result

    def Display(self):
        print("Stack data.")
        if self.Stack==[]:
            print("The stack is empty!")
        else:
            for data in reversed(self.Stack):
                print(data)

            print()


stack=Stack(int(input("Enter stack size:")))
while True:
    print("Chose an operation:")
    print("1.Push\n2.Pop\n3.Display\n4.Exit.")
    chose=int(input("Enter your chose:"))
    print()
    if chose is 1:
        for i in range(int(input("Enter number of push:"))):
            data=input("Enter data for stack:")
            stack.Push(data)
        stack.Display()
        print()

    elif chose is 2:
        n=stack.POP()
        if n is not -1:
            print("Deleted data:",n)
        stack.Display()

    elif chose is 3:
        stack.Display()

    elif chose is 4:
        print("Exiting..........")
        break
    else:
        print("Invalid input!")
        break


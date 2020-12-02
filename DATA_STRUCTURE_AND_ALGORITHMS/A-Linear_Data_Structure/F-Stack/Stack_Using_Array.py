#Implementation of Stack Using Array....By Dynamic Memory Allocation
class Stack:
    def __init__(self):
        self.Array=[]
        self.Top=-1

    def PusshData_In_Stack(self):
        item=int(input("Enter data:"))
        self.Top+=1
        self.Array.append(item)

    def PopData(self):
        x=0
        if self.Top==-1:
            print("Stack Underflow!")
        else:
            x=self.Array.pop()
            self.Top-=1
        return x

    def Check_Stack_Empty_Or_Not(self):
        if self.Top==-1:
            return True
        else:
            return False


    def Show_PeekData(self):
        if self.Top==-1:
            print("The stack is empty!")
        else:
            print("The peek value in the stack is:",self.Array[self.Top])
            print("The bottom value in the stack is:", self.Array[0])

    def display(self):
        if self.Top==-1:
            print("The stack is empty now!")
        else:
            temp = self.Top
            while temp >= 0:
                print(self.Array[temp])
                temp -= 1

            """ for i in range(self.Top,-1,-1):
                print(self.Array[i])
                print()
                
                for data in reversed(self.Array):
                print(data)"""

stk=Stack()
while True:
    print("Please,Chose an option:")
    print("1.Push")
    print("2.Pop")
    print("3.Show Peek/Top & Bottom data")
    print("4.Display")
    print("5.Check the stack is empty or not!")
    print("0.Logout")
    chose=int(input("Chose your option:"))
    print()
    if chose==1:
        while True:
            n = input("Do you want to Push?(Y/N):")
            if n.upper() == 'Y':
                stk.PusshData_In_Stack()

            elif n.upper() == "N":
                print("The stack is:")
                stk.display()
                break
            else:
                print("Invalid chose!")

    elif chose==2:
        while True:
            ch=input("Do you want to Pop?(Y/N):")
            if ch.upper()=="Y":
                s=stk.PopData()
                print("After Popped {} the stack is:".format(s))
                stk.display()
            elif ch.upper()=='N':
                break
            else:
                print("Invalid chose!")
    elif chose==3:
        stk.Show_PeekData()

    elif chose is 4:
        print("Final stack is:")
        stk.display()

    elif chose==5:
        if stk.Check_Stack_Empty_Or_Not() is True:
            print("The stack is empty!")
        else:
            print("The stack is not empty.")

    else:
        break



class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
class LinkedList_UsingStack:
    def __init__(self):
        self.top=None

    def Push(self,newnode):
        newnode.next=self.top
        self.top=newnode


    def Length(self):
        length=0
        temp=self.top
        while temp:
            temp=temp.next
            length+=1
        return length

    def PeekNode(self):
        if self.top is None:
            print("The stack is empty!")
        else:
            print("The top most element is:", self.top.Data)

    def Pop(self):
        temp=self.top
        if self.top is None:
            print("The stack is empty!")
        else:
            #print("Popped Node:",temp.Data)
            self.top=self.top.next
            del temp


    def dispaly(self):
        temp=self.top
        while temp:
            print(temp.Data)
            temp=temp.next
        print()


lst=LinkedList_UsingStack()
data=input("Enter data:").split()
for k in data:
    node=Node(k)
    lst.Push(node)
print("The list is:")
lst.dispaly()
print("After popped:")
lst.Pop()
lst.dispaly()

lst.PeekNode()
class CteateNodes:
    def __init__(self,data):
        self.Data=data
        self.next=None

class CreateLinkedlist:
    def __init__(self):
        self.head=None

    def AddNode(self,NewNode):
        if self.head is None:
            self.head=NewNode
        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=NewNode

    def ReversedList(self):
        if self.head is None:
            return
        else:
            PrevNode=None
            CurrentNode=self.head
            NextNode=self.head
            while NextNode is not None:
                NextNode=CurrentNode.next
                CurrentNode.next=PrevNode
                PrevNode=CurrentNode
                CurrentNode=NextNode
            self.head=PrevNode

    def Length(self):
        temp=self.head
        l=0
        while temp is not None:
            temp=temp.next
            l+=1
        return l

    def CheckEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def MiddleInsert(self,position):
        if position>=self.Length():
            print("Invalid position!")
        else:
            cpos=1
            current=self.head
            while cpos<position:
                current=current.next
                cpos+=1

            data=input("Enter data:")
            NewNode=CteateNodes(data)
            NewNode.next=current.next
            current.next=NewNode

    def LastInsertion(self,newNode):
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=newNode

    def FistInsertion(self,newnode):
        newnode.next=self.head
        self.head=newnode

    def Firstdeletion(self):
        temp=self.head
        self.head=self.head.next
        #temp.next=None
        del temp

    def Middledeletion(self,Position):
        if Position<=1 or Position>=self.Length():
            print("Invalid position!")
        else:
            currentPosition=1
            currentNode=self.head
            while currentPosition<Position-1:
                currentNode=currentNode.next
                currentPosition+=1
            nextNode=currentNode.next
            currentNode.next=nextNode.next
            del nextNode


    def Lastdeletion(self):
        lastNode=self.head
        previousNode=None
        while lastNode.next is not None:
            previousNode=lastNode
            lastNode=lastNode.next

        if lastNode==self.head:
            self.head=None      #if only 1 node in the list
        else:
          previousNode.next=None

        del lastNode


    def Display(self):
        current=self.head
        while current is not None:
            print(current.Data,end=" ")
            current=current.next
        print()

lst=CreateLinkedlist()
data=input("Enter data:").split()
for k in data:
    node=CteateNodes(k)
    lst.AddNode(node)
print("The list is:")
lst.Display()

print("After reversed list:",end=" ")
lst.ReversedList()
lst.Display()

n=int(input("Enter a position:"))
lst.MiddleInsert(n)
lst.Display()


if lst.CheckEmpty() is True:
    print("The list is empty!,Please create before.")
else:
    data = input("Enter data for last insertion:")
    node=CteateNodes(data)
    lst.LastInsertion(node)
    print("The list is:",end=" ")
    lst.Display()

node=CteateNodes(input("Enter 1st insertion data:"))
print("After 1st Insertion:",end=" ")
lst.FistInsertion(node)
lst.Display()


print("After 1st deletion:",end=" ")
lst.Firstdeletion()
lst.Display()


pos=int(input("Enter position:"))
print("Delete at position:")
lst.Middledeletion(pos)
lst.Display()

print("After last deletion:",end=" ")
lst.Lastdeletion()
lst.Display()
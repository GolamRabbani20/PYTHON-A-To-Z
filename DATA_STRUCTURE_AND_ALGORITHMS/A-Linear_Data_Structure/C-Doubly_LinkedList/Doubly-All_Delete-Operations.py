class CreateNode:
    def __init__(self,data):
        self.Data=data
        self.next=None
        self.prev=None

class CreateLinkedList:
    def __init__(self):
        self.head=None

    def NormalInsertion(self,newNode):
        if self.head is None:
            self.head=newNode
            self.head.next=None
            self.head.prev=None

        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=newNode
            newNode.prev=LastNode
            newNode.next=None

    def CheckEmpty_OR_Not(self):
        if self.head is None:
            return True
        else:
            return False

    def LengthOFList(self):
        CurrentNode=self.head
        Length=0
        while CurrentNode is not None:
            CurrentNode=CurrentNode.next
            Length+=1
        return Length

    def FirstDeletion(self):
        TempNode=self.head
        self.head=self.head.next
        self.head.prev=None
        print(self.head.next.Data)
        del TempNode

    def Middle_Deletion(self,POsition):
        CurrentNode=self.head
        CurrentPosition=1
        PreviousNode=None
        while CurrentNode:
            if CurrentPosition==POsition:
                PreviousNode.next=CurrentNode.next
                CurrentNode.next.prev=PreviousNode
                del CurrentNode
                break
            PreviousNode=CurrentNode
            CurrentNode=CurrentNode.next
            CurrentPosition+=1

    def LastDeletion(self):
        CurrentNode=self.head
        PreviousNode=None
        while CurrentNode.next is not None:
            PreviousNode=CurrentNode
            CurrentNode=CurrentNode.next
        PreviousNode.next=None
        del CurrentNode

    def FindMaxValue(self):
        Max=self.head.Data
        CurrentNode=self.head.next
        while CurrentNode is not None:
            if CurrentNode.Data>Max:
                Max=CurrentNode.Data
            CurrentNode=CurrentNode.next
        print(Max)

    def FindMinValue(self):
        Min = self.head.Data
        CurrentNode = self.head.next
        while CurrentNode is not None:
            if CurrentNode.Data < Min:
                Min = CurrentNode.Data
            CurrentNode = CurrentNode.next
        print(Min)


    def DisplayLinkedList(self):
        CreateNode=self.head
        while CreateNode is not None:
            print(CreateNode.Data,end=" ")
            CreateNode=CreateNode.next
        print()


lst=CreateLinkedList()
data=input("Enter data:").split()
for k in data:
    node=CreateNode(int(k))
    lst.NormalInsertion(node)
print("The created Linked List is:",end=" ")
lst.DisplayLinkedList()
print()

print("After 1st deletion:",end=" ")
lst.FirstDeletion()
lst.DisplayLinkedList()

print("After last deletion:",end=" ")
lst.LastDeletion()
lst.DisplayLinkedList()
print()

pos=int(input("Enter position:"))
print("After middle deletion:",end=" ")
lst.Middle_Deletion(pos)
lst.DisplayLinkedList()

print("The max value is:",end=" ")
lst.FindMaxValue()

print("The min value is:",end=" ")
lst.FindMinValue()
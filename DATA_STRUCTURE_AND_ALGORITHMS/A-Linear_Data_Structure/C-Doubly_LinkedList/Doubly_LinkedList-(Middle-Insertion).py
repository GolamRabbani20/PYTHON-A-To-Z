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

    def MiddleInsertion(self,Position,Middle_Node):
        CurrentNode=self.head
        PreviousNode=None
        CurrentPosition=0
        while CurrentNode is not None:
            if CurrentPosition==Position:
                PreviousNode.next=Middle_Node
                Middle_Node.prev = PreviousNode
                Middle_Node.next=CurrentNode
                CurrentNode.prev=Middle_Node
                break
            PreviousNode = CurrentNode
            CurrentNode=CurrentNode.next
            CurrentPosition+=1

    def DisplayLinkedList(self):
        CreateNode=self.head
        while CreateNode is not None:
            print(CreateNode.Data,end=" ")
            CreateNode=CreateNode.next
        print()

lst=CreateLinkedList()
data=input("Enter data:").split()
for k in data:
    node=CreateNode(k)
    lst.NormalInsertion(node)
print("The created Linked List is:",end=" ")
lst.DisplayLinkedList()
print()


if lst.CheckEmpty_OR_Not() is False:
    if lst.LengthOFList()>=2:
        data1 = input("Enter middle Insertion data:")
        position = int(input("Enter position:"))
        if position>0 and position<lst.LengthOFList():
            node = CreateNode(data1)
            lst.MiddleInsertion(position,node)
            print("After middle Insertion:",end=" ")
            lst.DisplayLinkedList()
        else:
            print("Invalid position!")
    else:
        print("There is less than 2 nodes,So middle insertion is not possible!")
else:
    print("Sorry the list is empty!")
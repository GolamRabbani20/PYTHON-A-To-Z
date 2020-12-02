class Nodes:
    def __init__(self,data):
        self.Data=data
        self.prev=None
        self.next=None

class LinkedList:
    def __init__(self):
       self.head=None

    def InsertNode(self,newNode):
        if self.head is None:
            self.head=newNode
            newNode.prev=None
            newNode.next=None
        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=newNode
            LastNode.prev=LastNode
            newNode.next=None

    def FirstInserTion(self,newNode):
        if self.head is None:
            self.head = newNode
            newNode.next=None
            newNode.prev=None
        else:
            tempNode=self.head
            self.head=newNode
            self.head.next=tempNode
            self.head.prev=None
            tempNode.prev=self.head


    def LastInsertion(self,newNodes):
        StartNode=self.head
        while StartNode.next is not None:
            StartNode=StartNode.next

        StartNode.next = newNodes
        newNodes.next = None
        newNodes.prev = StartNode
        #print("prev=",newNodes.prev.Data,"lop")

    def display(self):
        Current=self.head
        while Current is not None:
            print(Current.Data,end=" ")
            Current=Current.next
        print()

    def FindLargestValue_Method1(self):
        Large=self.head.Data
        CurrentNode=self.head.next
        while CurrentNode is not None:
            if CurrentNode.Data>Large:
                Large=CurrentNode.Data
            CurrentNode=CurrentNode.next
        print(Large)

def FindLargestValue_Mathod2(Double_LinkedList):
    LargeValue=Double_LinkedList.head.Data
    CurrentNode=Double_LinkedList.head.next
    while CurrentNode is not None:
        if CurrentNode.Data>LargeValue:
            LargeValue=CurrentNode.Data
        CurrentNode=CurrentNode.next
    return LargeValue


lst=LinkedList()
try:
    n=int(input("Enter number of Nodes:"))
    for i in range(n):
        data=int(input("Enter data:"))
        node=Nodes(data)
        lst.InsertNode(node)


    print("The list is:",end=" ")
    lst.display()

    print("The large node is(Method-1):",end=" ")
    lst.FindLargestValue_Method1()

    Large=FindLargestValue_Mathod2(lst)
    if Large:
        print("The Largest value in the list(Method-2):",Large)
    else:
        print("The List is empty!")

    k=int(input("Enter insertion data:"))
    print("After last insertion:",end=" ")
    node=Nodes(k)
    lst.LastInsertion(node)
    lst.display()

    d=int(input("1st Insertion data:"))
    node=Nodes(d)
    lst.FirstInserTion(node)
    print("After 1st insertion:",end=" ")
    lst.display()


except ValueError:
    print("Wrong input")


#Python Program to Reverse a Linked List
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def AppendNode(self,NewNode):
        if self.head is None:
            self.head=NewNode
        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=NewNode

    def Display(self):
        current=self.head
        while current:
            print(current.Data,end=" ")
            current=current.next
        print()

def ReversedList(List):
    temp=None
    current=List.head
    if current is None:
        return
    x=current.next
    while x:
        current.next=temp
        temp=current
        current=x
        x=x.next
    current.next=temp
    List.head=current


Lst=LinkedList()
data=input("Please enter the elements in the linked list:").split()
for k in data:
    node=Node(int(k))
    Lst.AppendNode(node)
Lst.Display()

ReversedList(Lst)
Lst.Display()
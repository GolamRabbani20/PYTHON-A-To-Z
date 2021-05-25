#Python Program to Print Middle most Node of a Linked List
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def AddNode(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=newNode

    def Length(self):
        Length=0
        current=self.head
        while current is not None:
            current=current.next
            Length+=1
        return Length

    def FindElement(self):
        current=self.head
        Length=self.Length()
        if Length%2:
            Len=Length//2
            for k in range(Len):
                current=current.next
            print(current.Data)
        else:
            Len=Length//2
            for k in range(1,Len+2):
                if k==Len or k==Len+1:
                    print(current.Data,end=" ")
                current=current.next


lst=LinkedList()
data = input("Please enter the elements in the linked list:").split()
for k in data:
    node=Node(k)
    lst.AddNode(node)
if lst.Length()%2:
    print("The middle element is",end=" ")
    lst.FindElement()
else:
    print("The two middle elements are", end=" ")
    lst.FindElement()
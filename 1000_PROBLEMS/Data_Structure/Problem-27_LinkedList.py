#Python Program to Print Nth Node from the last of a Linked List
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

    def FindElement(self,n):
        current=self.head
        Len=self.Length()
        for k in range(Len-n):
            current=current.next
        return current.Data

lst=LinkedList()
data = input("Enter data:").split()
for k in data:
    node=Node(k)
    lst.AddNode(node)
n=int(input("The nth element from the end will be printed. Please enter n:"))
print("The nth element from the end:",lst.FindElement(n))


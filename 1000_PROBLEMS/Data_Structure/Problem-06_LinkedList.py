#Python Program to Display all the Nodes in a Linked List using Recursion
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def AddNodes(self,newNode):
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head  #insert 1st
            self.head=newNode

    def display(self):
        self.display2(self.head)

    def display2(self,currentNode):
        if currentNode is None:
            return currentNode
        self.display2(currentNode.next)
        print(currentNode.Data,end=" ")

lst=LinkedList()
n=int(input("Enter node number:"))
for k in range(n):
    data=input("Enter value:")
    node=Node(data)
    lst.AddNodes(node)
print("The linked list is:",end=" ")
lst.display()
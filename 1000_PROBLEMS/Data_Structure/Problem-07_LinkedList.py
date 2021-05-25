#Python Program to Display the Nodes of a Linked List in Reverse without using Recursion
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
        currentNode=self.head
        while currentNode!=None:
            print(currentNode.Data,end=" ")
            currentNode=currentNode.next
        print()

lst=LinkedList()
n=int(input("Enter node number:"))
for k in range(n):
    data=input("Enter value:")
    node=Node(data)
    lst.AddNodes(node)
print("The linked list is:",end=" ")
lst.display()
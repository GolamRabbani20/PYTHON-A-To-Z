#Python Program to Display the Nodes of a Linked List in Reverse using Recursion
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def InsertNode(self,newNode):
        if self.head==None:
            self.head=newNode
        else:
            lastNode=self.head
            while lastNode.next is not None:
                lastNode=lastNode.next
            lastNode.next=newNode

    def dispaly(self):
        self.display2(self.head)

    def display2(self,currentNode):
        if currentNode is None:
            return currentNode
        self.display2(currentNode.next)
        print(currentNode.Data,end=" ")


linkedList=LinkedList()
n=int(input("Enter number of nodes:"))
while n>=1:
    data=input("Enter node value:")
    node=Node(data)
    linkedList.InsertNode(node)
    n-=1

linkedList.dispaly()

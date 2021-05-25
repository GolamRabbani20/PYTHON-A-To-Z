#Python Program to Create a Linked List & Display the Elements in the List
#Solution-01
'''
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.Last_Node=None
    def InsertNode(self,data):
        if self.Last_Node is None:
            self.head=Node(data)
            self.Last_Node=self.head
        else:
            self.Last_Node.next=Node(data)
            self.Last_Node=self.Last_Node.next

    def display(self):
        print("The linked list is:",end=" ")
        currentNade=self.head
        while currentNade!=None:
            print(currentNade.Data,end=" ")
            currentNade=currentNade.next

lst=LinkedList()
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=input("Enter value of node:")
    lst.InsertNode(data)

lst.display()

'''
class Nodes:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def NodeInsertion(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while lastNode.next!=None:
                lastNode=lastNode.next
            lastNode.next=newNode

    def printing(self):
        print("The Linked List is:",end=" ")
        currentNode=self.head
        while currentNode!=None:
            print(currentNode.Data,end=" ")
            currentNode=currentNode.next
        exit(0)

lst=LinkedList()
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=input("Enter value of nodes:")
    node=Nodes(data)
    lst.NodeInsertion(node)

lst.printing()

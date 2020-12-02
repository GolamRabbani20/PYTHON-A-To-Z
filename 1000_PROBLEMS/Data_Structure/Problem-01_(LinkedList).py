#Python Program to Read a Linked List in Reverse
#Solution_No-01
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
            newNode.next=self.head
            self.head=newNode
    def dispaly(self):
        print("The Linked List is:",end=" ")
        currentNode=self.head
        while currentNode!=None:
            print(currentNode.Data,end=" ")
            currentNode=currentNode.next


linkedList=LinkedList()
n=int(input("Enter number of nodes:"))
while n>=1:
    data=input("Enter node value:")
    node=Node(data)
    linkedList.InsertNode(node)
    n-=1

linkedList.dispaly()

'''
#Solutino-02 // Using First Insertion Method
class CreateNode:
    def __init__(self,data):
        self.Data=data
        self.next=None


class CreateLinkedList:
    def __init__(self):
        self.head=None

    def FirstInsertion(self,newNode):
        TempNode=self.head
        self.head=newNode
        self.head.next=TempNode
        del TempNode

    def display(self):
        print("The Linked List is: ",end="")
        currentNode=self.head
        while currentNode!=None:
            print(currentNode.Data,end=" ")
            currentNode=currentNode.next


LinkedList=CreateLinkedList()
n=int(input("Enter number of Nodes:"))
for i in range(n):
    data=input("Enter value:")
    node=CreateNode(data)
    LinkedList.FirstInsertion(node)

LinkedList.display()
'''
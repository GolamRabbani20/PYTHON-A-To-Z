#Python Program to Search for an Element in the Linked List without using Recursion
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def InsertNode(self,NewNode):
        if self.head is None:
            self.head=NewNode
        else:
            lastNode=self.head
            while lastNode.next is not None:
                lastNode=lastNode.next
            lastNode.next=NewNode

    def SearchNode(self,Item):
        length=0
        currentNode=self.head
        while currentNode is not None:
            if currentNode.Data==Item:
                return length
            currentNode=currentNode.next
            length+=1
        return -1


    def display(self):
        currentNode=self.head

        while currentNode is not None:
            print(currentNode.Data,end=" ")
            currentNode=currentNode.next
        print()

lst=LinkedList()
n=int(input("Number of Nodes:"))
for i in range(n):
    data=input("Enter value:")
    node=Node(data)
    lst.InsertNode(node)
print("The list is:",end=" ")
lst.display()

item=input("Enter a item:")
index=lst.SearchNode(item)
if index==-1:
    print(item,"is not found.")
else:
   print(item,"is found at index",index)
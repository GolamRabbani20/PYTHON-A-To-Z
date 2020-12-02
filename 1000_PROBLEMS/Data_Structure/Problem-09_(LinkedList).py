#Python Program to Find the Length of the Linked List without using Recursion
class Nodes:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def AddNodes(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode

    def Length(self):
        currentNode=self.head
        length=0
        while currentNode!=None:
            currentNode=currentNode.next
            length+=1
        return length

lst=LinkedList()
try:
    n=int(input("Enter number of nodes:"))
    for i in range(n):
        data=input("Enter value of nodes:")
        node=Nodes(data)
        lst.AddNodes(node)
except ValueError:
    print("Wrong input!")


print("\nLength of the Linked List:",end=" ")
print(lst.Length())

#Python Program to Count the Number of Occurrences of an Element in the Linked List without using Recursion
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
           lastNode=self.head
           while lastNode.next is not None:
               lastNode=lastNode.next
           lastNode.next=newNode

    def Alternate1(self):
        self.Alternate2(self.head)

    def Alternate2(self,CurrentNode):
        if CurrentNode is None:
            exit()
        print(CurrentNode.Data,end=" ")

        if CurrentNode.next:
           self.Alternate2(CurrentNode.next.next)



    def display(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.Data,end=" ")
            currentNode=currentNode.next
        print()


lst=LinkedList()

n=int(input("Enter number of nodes:"))
for i in range(n):
    data=input("Enter value of nodes:")
    node=Nodes(data)
    lst.AddNodes(node)

print("\nThe Linked List:",end=" ")
lst.display()
print("The Alternate Item in the list:",end=" ")
lst.Alternate1()

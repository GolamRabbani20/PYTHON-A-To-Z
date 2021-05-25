class Nodes:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
       self.head=None

    def InsertNode(self,newNode):
        if self.head is None:
            self.head=newNode

        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=newNode

    def displayLinkedList(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.Data,end=" ")
            currentNode=currentNode.next
        print()

    def DeleteLastNode(self):
        LastNode=self.head
        PreviousNode=None
        while LastNode.next is not None:
            PreviousNode = LastNode
            LastNode = LastNode.next

        PreviousNode.next =LastNode.next  #PreviousNode.next =None
        del LastNode


lst=LinkedList()
n=int(input("Enter number of nodes:"))

for i in range(n):
    data=input("Enter node's value:")
    node=Nodes(data)
    lst.InsertNode(node)

print("The Linked List is:",end=" ")
lst.displayLinkedList()

print("Afer deletion:",end=" ")
lst.DeleteLastNode()
lst.displayLinkedList()
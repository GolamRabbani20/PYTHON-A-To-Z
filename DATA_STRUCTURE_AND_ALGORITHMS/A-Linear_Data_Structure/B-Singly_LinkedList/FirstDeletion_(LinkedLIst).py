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


    def LengthOfLikedList(self):
        StartNode=self.head
        Length=0
        while StartNode is not None:
            StartNode=StartNode.next
            Length+=1
        return Length
    def Firstdeletion(self):
        FirstNode=self.head
        self.head=FirstNode.next
        del FirstNode


lst=LinkedList()

data=input("Enter node's value:").split()
for k in data:
    node=Nodes(k)
    lst.InsertNode(node)

print("The Linked List is:",end=" ")
lst.displayLinkedList()
print()


n=lst.LengthOfLikedList()
for k in range(n):
    if k<n-1:
        print("After 1st deletion:", end=" ")
        lst.Firstdeletion()
        lst.displayLinkedList()
    else:
        print("After 1st deletion: Empty")


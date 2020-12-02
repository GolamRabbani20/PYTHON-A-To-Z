#Python Program to Remove Duplicates from a Linked List
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def AppendNode(self,NewNode):
        if self.head is None:
            self.head=NewNode
        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=NewNode

    def Display(self):
        current=self.head
        while current:
            print(current.Data,end=" ")
            current=current.next
        print()

    def removeDuplicate1(self):
        current = self.head
        prevNode = None
        while current:
            current1 = current.next
            while current1:
                if current.Data == current1.Data:
                    prevNode.next = current.next
                current1 = current1.next
            prevNode = current
            current = current.next
            

def removeDuplicate(List):
    current=List.head
    prevNode=None
    while current:
       current1=current.next
       while current1:
            if current.Data==current1.Data:
                prevNode.next=current.next
            current1=current1.next
       prevNode = current
       current=current.next




Lst1=LinkedList()
data=input("Please enter the elements in the linked list:").split()
for k in data:
    node=Node(int(k))
    Lst1.AppendNode(node)


print("The list with duplicates removed(out of class):",end=" ")
removeDuplicate(Lst1)
Lst1.Display()

print("The list with duplicates removed(In class):",end=" ")
#removeDuplicate1()
Lst1.Display()


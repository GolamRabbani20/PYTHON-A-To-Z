class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.tail=None

    def AddNode(self,newNode):
        if self.tail is None:
            self.tail=newNode
            newNode.next=self.tail

        else:
            newNode.next=self.tail.next
            self.tail.next = newNode
            self.tail=newNode

    def Reversed(self):
        if self.tail is None:
            return
        else:
            Prev=None
            Current=self.tail.next
            NextNode=Current.next
            while Current is not self.tail:
                Prev=Current
                Current=NextNode
                NextNode=Current.next
                Current.next=Prev
            NextNode.next=Current
            self.tail=NextNode


    def display(self):
        current=self.tail.next
        while current is not self.tail:
            print(current.Data,end=" ")
            current=current.next
        print(current.Data)

lst=CircularLinkedList()
data=input("Enter data:").split()
for k in data:
    node=Node(k)
    lst.AddNode(node)
print("The circular linked list:",end=" ")
lst.display()
print()
print("After reversed:",end=" ")
lst.Reversed()
lst.display()
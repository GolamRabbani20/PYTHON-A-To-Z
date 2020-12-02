class Nodes:
    def __init__(self,data):
        self.Data=data
        self.next=None
class LinkedLit:
    def __init__(self):
        self.head=None

    def InsertNodes(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=newNode

    def display(self):
        CurrentNode=self.head
        while CurrentNode is not None:
            print(CurrentNode.Data,end=" ")
            CurrentNode=CurrentNode.next
        print()

    def FindLargestNode(self):
        LargeNode=self.head.Data
        CurrentNode=self.head.next
        while CurrentNode is not None:
            if CurrentNode.Data>LargeNode:
                 LargeNode=CurrentNode.Data
            CurrentNode=CurrentNode.next
        print(LargeNode)

lst=LinkedLit()
n=int(input("Enter number of node:"))
for k in range(n):
    data=int(input("Enter node data:"))
    node=Nodes(data)
    lst.InsertNodes(node)
print("The list is:",end=" ")
lst.display()

print("The large node is:",end=" ")
lst.FindLargestNode()


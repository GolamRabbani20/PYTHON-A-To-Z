class CreateNode:
    def __init__(self,data):
        self.Data=data
        self.next=None

class CreateLinkedList:
    def __init__(self):
        self.head=None
        self.lastNode=None


    def InsertNode(self,newNode):
         if self.head is None:
             self.head=newNode
             self.lastNode=newNode
         else:
             self.Length=1
             self.lastNode.next=newNode
             self.lastNode=newNode


    def LastInsertion(self,newNode):
        self.lastNode.next=newNode
        self.lastNode=newNode


    def displayLinkedList(self):
          currentNode=self.head
          while currentNode !=None:
              print(currentNode.Data,end=" ")
              currentNode=currentNode.next
          print()

linklist=CreateLinkedList()
n=input("Enter number of node:").split()
for k in n:
    node=CreateNode(k)
    linklist.InsertNode(node)
print("The Linked List is:",end=" ")
linklist.displayLinkedList()

k=CreateNode(20)
linklist.LastInsertion(k)
linklist.displayLinkedList()

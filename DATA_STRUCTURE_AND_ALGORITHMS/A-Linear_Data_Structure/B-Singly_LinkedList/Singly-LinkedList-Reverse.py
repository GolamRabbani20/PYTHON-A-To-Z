class CreateNode:
    def __init__(self,data):
        self.Data=data
        self.next=None

class CreateLinkedList:
    def __init__(self):
        self.head=None  #head is not a node,Head is a initial pointer

    def InsertNode(self,newNode):
         if self.head is None:
             self.head=newNode
         else:
             lastNode=self.head   #head pointer point kore ase 1st node k #Now 1st node=Last Node
             while lastNode.next !=None:
                 lastNode=lastNode.next
             lastNode.next=newNode

    def ReversedList(self):
        if self.head is None:
            return
        prevNode=None
        CurrentNode=self.head
        NextNode=self.head
        while NextNode is not None:
            NextNode=CurrentNode.next
            CurrentNode.next=prevNode
            prevNode=CurrentNode
            CurrentNode=NextNode
        self.head=prevNode


    def displayLinkedList(self):
          currentNode=self.head
          while currentNode !=None:
              print(currentNode.Data,end=" ")
              currentNode=currentNode.next

          print()

linklist=CreateLinkedList()
data=input("Enter data:").split()
for k in data:
    node=CreateNode(k)
    linklist.InsertNode(node)
print("The Linked List is:",end=" ")
linklist.displayLinkedList()

print("After reverse:",end=" ")
linklist.ReversedList()
linklist.displayLinkedList()

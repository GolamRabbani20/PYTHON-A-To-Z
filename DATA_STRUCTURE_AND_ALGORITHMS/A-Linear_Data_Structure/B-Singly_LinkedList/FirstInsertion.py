#First Insertion

#Create node
#Create Linked List
#Insert the node in the Linked List
#Print the linked List
class Node:
  def __init__(self,data):
    self.Data=data
    self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def FirstInsertion(self,newNode):
        newNode.next=self.head
        self.head=newNode

    def InsertNode(self,newNode):
        if self.head is None:
            self.head=newNode

        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=newNode

    def display(self):
        currentNode=self.head
        while currentNode!=None:
            print(currentNode.Data)
            currentNode=currentNode.next
        print()

linklist=LinkedList()

data=input("Enter a data:")
node=Node(data)
#print(node)
linklist.InsertNode(node)
print()

n=int(input("Enter number of nodes:"))
for k in range(n):
    data=input("Enter data:")
    node=Node(data)
    #print(node)
    linklist.FirstInsertion(node)

print("The Linked List is:")
linklist.display()


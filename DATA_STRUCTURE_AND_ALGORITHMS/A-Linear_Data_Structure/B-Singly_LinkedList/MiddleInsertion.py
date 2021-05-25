class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def LengthOfLinkedList(self):
        currentNode=self.head
        Lenght=0
        while currentNode is not None:
            Lenght+=1
            currentNode=currentNode.next
        return Lenght


    def LastInsertion(self,newNode):
         if self.head is None:
             self.head=newNode
         else:
            EndNode=self.head
            while EndNode.next!=None:
                EndNode=EndNode.next
            EndNode.next=newNode

    def MiddleInsertion(self,midNode,position):
        currentNode=self.head
        previousNode=None
        currentPosition=0
        if self.LengthOfLinkedList()<=1:
            print("Middle Insertion is not possible!")
        else:
            if position<0 or position>=self.LengthOfLinkedList():
                print("Invalid position!")
                return
            while currentNode:
                if currentPosition==position:
                    previousNode.next=midNode
                    midNode.next=currentNode
                    break
                previousNode=currentNode
                currentNode=currentNode.next
                currentPosition+=1

    def display(self):
        currentNode=self.head
        while currentNode!=None:
            print(currentNode.Data,end=" ")
            currentNode=currentNode.next
        print()
        #exit(0)


lst=LinkedList()
n=int(input("Enter Number nodes:"))
for i in range(n):
    data=int(input("Enter node's value:"))
    node=Node(data)
    lst.LastInsertion(node)
print("Before middle Insertion the List is:",end=" ")
lst.display()

midNode=input("Enter mid value:")
position=int(input("Enter position:"))
node=Node(midNode)
lst.MiddleInsertion(node,position)
print("After middle Insertion the list is:",end=" ")
lst.display()
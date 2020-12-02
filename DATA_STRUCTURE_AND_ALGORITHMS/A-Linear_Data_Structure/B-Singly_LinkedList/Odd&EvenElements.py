class Nodes:
    def __init__(self,data):
        self.Data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def InsertLinkedList(self,NewNode):
        if self.head==None:
            self.head=NewNode
        else:
            lastNode=self.head
            while lastNode.next is not None:
                lastNode=lastNode.next
            lastNode.next=NewNode
    def display(self):
        current=self.head
        while current!=None:
            print(current.Data,end=" ")
            current=current.next

    def EvenElement(self):
        self.EvenElement2(self.head)

    def EvenElement2(self,currentNode):
        if currentNode == None:
            return
        elif currentNode.Data%2 is 0:
            print(currentNode.Data,end=" ")
            self.EvenElement2(currentNode.next)

        else:
            self.EvenElement2(currentNode.next)


    def OddElements(self):
        self.OddElements2(self.head)

    def OddElements2(self,startNode):
        if startNode is None:
            return
        elif startNode.Data%2:
            print(startNode.Data,end=" ")
            self.OddElements2(startNode.next)
        else:
            self.OddElements2(startNode.next)

    def someOfNodes(self):
        print(self.SomeOfNodes(0,self.head))

    def SomeOfNodes(self,Sum,CurrentNode):
        if CurrentNode is None:
            return Sum
        return self.SomeOfNodes(Sum+CurrentNode.Data,CurrentNode.next)

lst=LinkedList()
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=int(input("Enter value:"))
    node=Nodes(data)
    lst.InsertLinkedList(node)

print("The list is:",end=" ")
lst.display()
print()
print("The Even elements of the list:",end=" ")
lst.EvenElement()

print()
print("The Odd elements of the list:",end=" ")
lst.OddElements()
print()
print("Sum of Elements:",end=" ")
lst.someOfNodes()
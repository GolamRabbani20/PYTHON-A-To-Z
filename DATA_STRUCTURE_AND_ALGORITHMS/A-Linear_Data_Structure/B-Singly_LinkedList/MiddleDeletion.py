class Nodes:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
       self.head=None

    def CheckEmpty_Or_Not(self):
        if self.head is None:
            return True
        else:
            return False

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


    def MeddleDeletion_Using_Positin(self,Position):
        if self.CheckEmpty_Or_Not() is False:
            if self.LengthOfLikedList()>2:
                CurrentNode = self.head
                CurrentPostion = 1
                PreviousNode = None
                while CurrentNode.next is not None:
                     if CurrentPostion==Position:
                         PreviousNode.next=CurrentNode.next
                         del CurrentNode.next
                         del CurrentNode
                         break
                     PreviousNode = CurrentNode
                     CurrentPostion+=1
                     CurrentNode=CurrentNode.next
            else:

                print("Middle Deletion is not possible! Because there are less than 3 node.")
                return
        else:
            print("The list is Empty!")
            return

    def Deletion_MiddleNode_Using_NodeValue(self,NodeData):
        if self.CheckEmpty_Or_Not() is False:
            StartNode = self.head.next
            PreviousNode = None
            if self.head.Data==NodeData:
                print("Invalid Value! You can not delete first node.")
                return
            else:
                while StartNode.next is not None:
                    if StartNode.Data==NodeData:
                        PreviousNode.next=StartNode.next
                        del StartNode.Data
                        break

                    PreviousNode=StartNode
                    StartNode=StartNode.next
                else:
                    print("Invalid Value! You can not delete last node.")
                    return
        else:
            print("The Linked List is Empty!")

lst=LinkedList()
n=int(input("Enter number of nodes:"))

for i in range(n):
    data=input("Enter node's value:")
    node=Nodes(data)
    lst.InsertNode(node)

print("The Linked List is:",end=" ")
lst.displayLinkedList()

pos=int(input("Enter position:"))
if pos<=1 or pos>=lst.LengthOfLikedList():
    print("Invalid position!")
else:
    lst.MeddleDeletion_Using_Positin(pos)
    print("After deletion using position:",end=" ")
    lst.displayLinkedList()

value=input("Enter delete by value:")
lst.Deletion_MiddleNode_Using_NodeValue(value)
print("After deleting value the list is:",end=" ")
lst.displayLinkedList()

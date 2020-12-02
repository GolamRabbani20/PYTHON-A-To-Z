#Python Program to Add Corresponding Positioned Elements of 2 Linked Lists
class Node:
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

    def Display(self):
        CurrentNode=self.head
        while CurrentNode is not None:
            print(CurrentNode.Data,end=" ")
            CurrentNode=CurrentNode.next
        print()

def Sum_Of_Linked_List(List1,List2):
    Sum_Of_Node=LinkedList()
    Current1=List1.head
    Current2=List2.head
    while Current1 and Current2:
        sum=Current1.Data+Current2.Data
        Sum_Of_Node.InsertNode(Node(sum))
        Current1=Current1.next
        Current2=Current2.next

    if Current1 is None:
        while Current2:
            Sum_Of_Node.InsertNode(Node(Current2.Data))
            Current2=Current2.next
    else:
        while Current1:
            Sum_Of_Node.InsertNode(Node(Current1.Data))
            Current1=Current1.next

    return Sum_Of_Node


lst1=LinkedList()
lst2=LinkedList()
data=input("Please enter the elements in the 1st linked list:").split()
for k in data:
    node=Node(int(k))
    lst1.InsertNode(node)

data=input("Please enter the elements in the 2nd linked list:").split()
for k in data:
    node=Node(int(k))
    lst2.InsertNode(node)

Sum_List=Sum_Of_Linked_List(lst1,lst2)
print("The new list is:",end=" ")
Sum_List.Display()

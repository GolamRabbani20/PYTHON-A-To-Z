#Python Program to Find the first Common Element between the 2 given Linked Lists
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

"""def Find_First_Common_Element(List1,List2):
    current1=List1.head
    c=0
    while current1:
        current2 = List2.head
        while current2:
            if current1.Data == current2.Data:
                print("The element that appears first in the first linked list that is common to both is:",current1.Data,end=" ")
                c+=1
                break
            current2=current2.next
        if c:
            break
        else:
         current1=current1.next
    if c is 0:
        print("The two lists have no common elements.")"""

def Find_First_Common_Element1(List1,List2):
    current1=List1.head
    while current1:
        current2 = List2.head
        while current2:
            if current1.Data==current2.Data:
              return current1.Data
            current2=current2.next
        current1=current1.next
    return None

Lst1=LinkedList()
Lst2=LinkedList()
data=input("Enter value for list1:").split()
for k in data:
    node=Node(int(k))
    Lst1.AppendNode(node)

data=input("Enter value for list1:").split()
for k in data:
    node=Node(int(k))
    Lst2.AppendNode(node)

Temp=Find_First_Common_Element1(Lst1,Lst2)
if Temp:
    print("The element that appears first in the first linked list that is common to both is:",Temp)
else:
    print("The two lists have no common elements.")



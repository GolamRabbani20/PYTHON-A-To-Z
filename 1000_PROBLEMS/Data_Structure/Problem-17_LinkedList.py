#Python Program to Check whether 2 Linked Lists are Same
class Nodes:
    def __init__(self,data):
        self.Data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def InsertNodes(self,NewNode):
        if self.head==None:
            self.head=NewNode
        else:
            LastNode=self.head
            while LastNode.next!=None:
                LastNode=LastNode.next
            LastNode.next=NewNode

    def displayList(self):
        CurrentNode=self.head
        while CurrentNode!=None:
            print(CurrentNode.Data,end=" ")
            CurrentNode=CurrentNode.next
        print()

def CalculateLength(lst1,lst2):
    current1=lst1.head
    current2=lst2.head

    while (current1 and current2):
        if current1.Data!=current2.Data:
            return False
        current1=current1.next
        current2=current2.next
    if current1 is None and current2 is None: #Checking the length are same or not
        return True
    else:
        return False


lst1=LinkedList()
lst2=LinkedList()
data1=input("Enter data for linked List-1:").split()
for k in data1:
    node=Nodes(k)
    lst1.InsertNodes(node)

print("The 1st Linked List is:",end=" ")
lst1.displayList()
print()

data2=input("Enter data for linked List-2:").split()
for k in data2:
    node=Nodes(k)
    lst2.InsertNodes(node)

print("The 2nd Linked List is:",end=" ")
lst2.displayList()

if CalculateLength(lst1,lst2):
    print("The two list are same.")
else:
    print("The two list are not same.")

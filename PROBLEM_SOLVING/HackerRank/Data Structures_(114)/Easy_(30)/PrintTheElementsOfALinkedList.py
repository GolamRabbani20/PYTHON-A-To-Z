from numpy import random as rdm
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
class CreateLink:
    def __init__(self):
        self.head=None
        self.tail=None

    def Insert(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            self.tail.next=newnode
        self.tail=newnode


    def display(self):
        while (self.head.next != None):
            print(self.head.Data)
            self.head = self.head.next
        print(self.head.Data)

lst=CreateLink()
for i in range(rdm.randint(1,1000)):
    data=rdm.randint(1,1000)
    node=Node(data)
    lst.Insert(node)
lst.display()

"""
#Solution
def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next
"""
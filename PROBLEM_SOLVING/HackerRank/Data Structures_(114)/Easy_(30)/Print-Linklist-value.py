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
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode


    def display(self):
        while (self.head.next != None):
            print(self.head.Data,end=" ")
            self.head = self.head.next
        print(self.head.Data)

lst=CreateLink()
for i in range(int(input())):
    data=int(input())
    node=Node(data)
    lst.Insert(node)
lst.display()


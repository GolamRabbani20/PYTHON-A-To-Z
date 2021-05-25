class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def CreateNode(self,NewNode):
        if self.head is None:
            self.head=NewNode
            self.tail=NewNode
        else:
           self.tail.next=NewNode
           NewNode.prev=self.tail
           self.tail=NewNode

    def ReversedList(self):
        Current=self.head
        while Current is not None:
            nextNode=Current.next
            Current.next=Current.prev
            Current.prev=nextNode
            Current=nextNode
        Current=self.tail
        self.tail=self.head
        self.head=Current

    def Length(self):
        current=self.head
        Len=0
        while current is not None:
            current=current.next
            Len+=1
        return Len


    def Firstdeletion(self):
        if self.tail==self.head:
            temp=self.head
            self.head=None
            self.tail=None
            del temp
        else:
            temp=self.head
            self.head=temp.next
            self.head.prev=None
            del temp

    def Lastdeletion(self):
        if self.tail==self.head:
            temp=self.head
            self.head=None
            self.tail=None
            del temp
        else:
            temp=self.tail
            self.tail=temp.prev
            self.tail.next=None
            del temp


    def DeleteAnynode(self,position):
        if position>1 and position<self.Length():
            temp = self.head
            i = 1
            while i < position:
                temp = temp.next
                i += 1
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            del temp

        elif position==1:
            #self.Firstdeletion()
            if self.tail == self.head:
                temp = self.head
                self.head = None
                self.tail = None
                del temp
            else:
                temp = self.head
                self.head = temp.next
                self.head.prev = None
                del temp

        elif position==self.Length():
            #self.Lastdeletion()
            if self.tail == self.head:
                temp = self.head
                self.head = None
                self.tail = None
                del temp
            else:
                temp = self.tail
                self.tail = temp.prev
                self.tail.next = None
                del temp

        else:
            print("Invalid position!")



    def Display(self):
        Current=self.head
        while Current is not None:
            print(Current.Data,end=" ")
            Current=Current.next
        print()

lst=DoublyLinkedList()
data=input("Enter data:").split()
for k in data:
    node=Node(k)
    lst.CreateNode(node)
print("The list is:",end=" ")
lst.Display()

print("After reversed:",end=" ")
lst.ReversedList()
lst.Display()

lst.Firstdeletion()
lst.Display()



while True:

    if lst.Length()>0:
        pos = int(input("Enter position:"))
        lst.DeleteAnynode(pos)
        lst.Display()
    else:
        print("The list is empty!")
        break


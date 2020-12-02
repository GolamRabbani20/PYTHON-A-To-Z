class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
        self.prev=None

class Doubly_Circular:
    def __init__(self):
        self.head=None
        self.tail=None

    def AddNode(self,newNode):
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.head.next=newNode
            self.head.prev=newNode

        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            newNode.next=self.head
            self.head.prev=newNode
            self.tail = newNode

    def Insert_At_Begin(self,newNode):
        newNode.next = self.head
        self.head.prev = newNode
        newNode.prev = self.tail
        self.tail.next = newNode
        self.head=newNode

    def Delete_At_Begin(self):
        temp=self.head
        self.head=self.head.next
        self.head.prev=self.tail
        self.tail.next=self.head
        del temp

    def Length(self):
        Len=0
        current=self.head
        while current is not self.tail:
            current=current.next
            Len+=1
        return Len+1

    def Insert_At_End(self,newNode):
        self.tail.next=newNode
        newNode.prev=self.tail
        newNode.next=self.head
        self.head.prev=newNode
        self.tail=newNode

    def Delete_At_End(self):
        temp=self.tail
        self.tail=temp.prev
        self.tail.next=self.head
        self.head.prev=self.tail
        del temp


    def Insert_After_Position(self,position):
        if self.head is None:
            print("The list is empty!")
        else:
            if position<=1 or position>=self.Length():
                print("Invalid Position!")

            else:
                cpos=1
                current=self.head
                while cpos<position:
                    current=current.next
                    cpos+=1
                newNode=Node(input("Enter data:"))
                newNode.next=current.next
                current.next.prev=newNode
                current.next=newNode
                newNode.prev=current

    def ReversedList(self):
        Current=self.head
        nextNode=None
        while Current is not self.tail:
            nextNode=Current.next
            Current.next=Current.prev
            Current.prev=nextNode
            Current=nextNode
        Current.prev=self.head
        Current.next=self.tail
        self.head=self.tail
        self.tail=nextNode

    def Delete_At_Position(self,position):
        if self.head is None:
            print("The list is empty!")
        else:
            if position<=1 or position>=self.Length():
                print("Invalid Position!")

            else:
                cpos=1
                current=self.head
                while cpos<position:
                    current=current.next
                    cpos+=1
                current.prev.next = current.next
                current.next.prev = current.prev
                del current

            """ cpos=1
                current=self.head
                while cpos<position-1:
                    current=current.next
                    cpos+=1
                temp=current.next
                current.next=temp.next
                temp.next.prev=current
                del temp"""

    def display(self):
        current=self.head
        while current is not self.tail:
            print(current.Data,end=" ")
            current=current.next
        print(current.Data)

        #print(self.tail.next.Data)
        #print(self.head.prev.Data)


lst=Doubly_Circular()
data=input("Enter data:").split()
for k in data:
    node=Node(k)
    lst.AddNode(node)
print("The circular linked list:",end=" ")
lst.display()
print()

data=input("Enter begin data:")
node=Node(data)
lst.Insert_At_Begin(node)
print("After insert at begin:",end=" ")
lst.display()

data=input("Enter End data:")
node=Node(data)
lst.Insert_At_End(node)
print("After insert at End:",end=" ")
lst.display()

n=int(input("Enter position:"))
lst.Insert_After_Position(n)
print("After insert specific position:",end=" ")
lst.display()

print("Length=",lst.Length())


lst.Delete_At_Begin()
print("After delete at begin:",end=" ")
lst.display()

lst.Delete_At_End()
print("After delete at End:",end=" ")
lst.display()

n=int(input("Enter position:"))
lst.Delete_At_Position(n)
print("After insert specific position:",end=" ")
lst.display()

print("After reversed:",end=" ")
lst.ReversedList()
lst.display()
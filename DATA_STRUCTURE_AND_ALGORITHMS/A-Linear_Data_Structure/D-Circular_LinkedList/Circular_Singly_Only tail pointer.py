class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
class Circular_Singly_Using_Only_Tail_Pointer:
    def __init__(self):
        self.tail=None
    def InsertNode(self,newNode):
        if self.tail==None:
            self.tail=newNode
            self.tail.next=newNode
        else:
            newNode.next=self.tail.next
            self.tail.next=newNode
            self.tail=self.tail.next #self.tail=newNode

    def length(self):
        current=self.tail.next
        length=0
        while current is not self.tail:
            current=current.next
            length+=1
        return length+1

    def Insert_at_Begin(self,newNode):
        if self.tail is None:
            self.tail=newNode
            newNode.next=self.tail
        else:
            newNode.next=self.tail.next
            self.tail.next=newNode

    def Insert_at_End(self, newNode):
        if self.tail is None:
            self.tail = newNode
            newNode.next = self.tail
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail=newNode

    def Insert_After_Position(self,position):
        if position<=1 or position>=self.length():
            print("Invalid position!")
        else:
            i=1
            temp=self.tail.next
            while i<position:
                temp=temp.next
                i+=1
            NewNode=Node(input("Enter data:"))
            NewNode.next=temp.next
            temp.next=NewNode

    def Delete_First_node(self):
        temp=self.tail
        if self.tail==None:
            print("Empty!")

        elif self.tail==self.tail.next:
            self.tail=None
            del temp
        else:
            temp=temp.next
            self.tail.next=temp.next
            del temp

    def Delete_Last_node(self):
        temp=self.tail
        if self.tail == None:
            print("Empty!")

        elif self.tail == self.tail.next:
            self.tail = None
            del temp

        else:
            while self.tail.next is not temp:
                self.tail=self.tail.next
            self.tail.next=temp.next
            del temp
    def Delete_At_Any_node(self,position):
        current=self.tail.next
        i=1
        while i<position-1:
            current=current.next
            i+=1
        nextNode=current.next
        current.next=nextNode.next
        del nextNode



    def display(self):
        temp=self.tail.next
        while temp.next is not self.tail.next:
            print(temp.Data,end=" ")
            temp=temp.next
        print(temp.Data)

lst=Circular_Singly_Using_Only_Tail_Pointer()
data = input("Enter data:").split()
for k in data:
    node = Node(k)
    lst.InsertNode(node)

print("length=",lst.length())

print("The list is:", end=" ")
lst.display()

data=input("Enter begin data:")
node=Node(data)
lst.Insert_at_Begin(node)
lst.display()

pos=int(input("Enter position:"))
lst.Insert_After_Position(pos)
print("After inserting after position:",end=" ")
lst.display()

data=input("Enter end data:")
node=Node(data)
lst.Insert_at_End(node)
lst.display()

print("After deleting 1st node:",end=" ")
lst.Delete_First_node()
lst.display()

print("After deleting last node:",end=" ")
lst.Delete_Last_node()
lst.display()

n=int(input("Enter a position:"))
lst.Delete_At_Any_node(n)
print("After deleting any node:",end=" ")
lst.display()
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None

class Circular_LinkedList_Using_Iteration:
    def __init__(self):
        self.head=None
        #self.tail=None

    def InsertNode(self,newNode):
        if self.head is None:
            self.head=newNode
            #self.tail=newNode
        else:
            LastNode=self.head
            while LastNode.next is not self.head:
                LastNode=LastNode.next
            LastNode.next=newNode
        newNode.next=self.head


    def Insert_at_Begin(self,newNode):
        temp=self.head
        while temp.next is not self.head:
            temp=temp.next
        temp.next=newNode
        newNode.next=self.head
        self.head=newNode



    def display(self):
        current=self.head
        while current.next is not self.head:
            print(current.Data,end=" ")
            current=current.next
        print(current.Data)



class Circular_LinkedList_Using_Tail:
    def __init__(self):
        self.head=None
        self.tail=None

    def InsertNode(self,newNode):
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.tail.next=self.head



    def Insert_at_Begin(self,newNode):
        self.tail.next=newNode
        newNode.next=self.head
        self.head=newNode



    def display(self):
        current=self.head
        while current.next is not self.head:
            print(current.Data,end=" ")
            current=current.next
        print(current.Data)


#=======================================================================================================
print("Circular_LinkedList_Using_Iteration")
lst=Circular_LinkedList_Using_Iteration()

data=input("Enter data:").split()
for k in data:
    node=Node(k)
    lst.InsertNode(node)

print("The list is:",end=" ")
lst.display()

data=input("Enter a data:")
node=Node(data)
lst.Insert_at_Begin(node)
lst.display()
print()
#===========================================================================================================
print("Circular_LinkedList_Using_Tail Pointer")
lst2=Circular_LinkedList_Using_Tail()
data=input("Enter data:").split()
for k in data:
    node=Node(k)
    lst2.InsertNode(node)

print("The list is:",end=" ")
lst2.display()

data=input("Enter a data:")
node=Node(data)
lst2.Insert_at_Begin(node)
lst2.display()
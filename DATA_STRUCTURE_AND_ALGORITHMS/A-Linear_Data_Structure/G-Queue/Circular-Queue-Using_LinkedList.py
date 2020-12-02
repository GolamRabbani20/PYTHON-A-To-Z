class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None

class Circular_Queue_Using_LinkedList:
    def __init__(self):
        self.Front=None
        self.Rear=None

    def EnqueueNode(self,newNode):
        if self.Front is None and self.Rear is None:
            self.Front=newNode
            self.Rear=newNode
            self.Rear.next=newNode

        else:
            self.Rear.next=newNode
            self.Rear=newNode
            newNode.next=self.Front

    def DequeueNode(self):
        temp = self.Front
        if self.Front is None and self.Rear is None:
            print("Underflow!\n")

        elif self.Rear==self.Front:
            self.Rear=None
            self.Front=None
            del temp

        else:
            self.Front=self.Front.next
            self.Rear.next=self.Front
            del temp

    def PeekNode(self):
        if self.Rear is None and self.Front is None:
            print("The queue is empty!\n")

        else:
            print("The top most front node is:",self.Front.Data)

    def display(self):
        if self.Rear is None and self.Front is None:
            print("The queue is empty!\n")

        else:
            temp=self.Front
            while temp.next != self.Front:
                print(temp.Data)
                temp=temp.next
            print(temp.Data)
            print()



k=Circular_Queue_Using_LinkedList()
data=input("Enter data:").split()
for i in data:
    node=Node(i)
    k.EnqueueNode(node)

print("The queue is:")
k.display()

while True:
    print("1.Enqueque Node")
    print("2.Dequeque Node")
    print("3.Display")
    print("4.Peek node")
    print("5.Log out")
    chose=int(input("Chose your option:"))
    print()

    if chose is 1:
        k.EnqueueNode(Node(input("Enter data:")))
        print("After enqueuing:")
        k.display()

    elif chose is 2:
        print("After dequeue:")
        k.DequeueNode()
        k.display()

    elif chose is 3:
        print("The final queue:")
        k.display()

    elif chose is 4:
        k.PeekNode()

    elif chose is 5:
        print("Logging out.....")
        break

    else:
        print("Invalid Chose!")
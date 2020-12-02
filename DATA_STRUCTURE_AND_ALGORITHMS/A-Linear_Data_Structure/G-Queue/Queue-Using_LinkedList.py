class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None

class Queue_Using_LinkedList:
    def __init__(self):
        self.front=None
        self.rear=None

    def EnqueueNode(self,newNode):
        if self.front==None and self.rear==None:
            self.front=newNode
            self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode

    def DequeueNode(self):
        if self.front==None and self.rear==None:
            print("Underflow!")

        elif self.front==self.rear:
            print("Dequeued value is:",self.front.Data)
            self.rear=None
            temp1=self.front
            self.front=None
            del temp1
        else:
            print("Dequeued value is:", self.front.Data)
            temp=self.front
            self.front=self.front.next
            del temp

    def ForntNode(self):
        if self.front==-1 and self.rear==-1:
            print("Empty!")
        else:
            print("The peek node is:",self.front.Data)

    def display(self):
        if self.front==None and self.rear==None:
            print("Queue is empty!")

        else:
            temp=self.front
            while temp:
                print(temp.Data)
                temp=temp.next

q=Queue_Using_LinkedList()
data=input("Enter data:").split()
for k in data:
    node=Node(k)
    q.EnqueueNode(node)

print("The queue is:")
q.display()


q.DequeueNode()
q.DequeueNode()
print("After dequeue node:")
q.display()

q.ForntNode()

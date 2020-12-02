class Queue:
    def __init__(self,size):
        self.Array=[]
        self.Size=size
        self.Front=-1
        self.Rear=-1

    def EnqueuqElement(self,Item):
        if self.Rear==self.Size-1:
            print("Queue is overflow now!")

        elif self.Front==-1 and self.Rear==-1:
            self.Rear=0
            self.Front=0
            self.Array.append(Item)
        else:
            self.Rear += 1
            self.Array.append(Item)

    def DequeueEnlement(self):
        if self.Front==-1 and self.Rear==-1:
            print("he queue is underflow now!")

        elif self.Front==self.Rear:
             self.Front=-1
             self.Rear=-1

        else:
            self.Front+=1

    def EmptyOR_NoT(self):
        if self.Front==-1 and self.Rear==-1:
            return True
        else:
            return False

    def Full_Or_Not(self):
        if self.Rear==self.Size-1:
            return True
        else:
            return False

    def ForntElement(self):
        if self.Front==-1 and self.Rear==-1:
            print("Empty!")
        else:
            print("The front element is:",self.Array[self.Front])

    def display(self):
        if self.Front==-1 and self.Rear==-1 or self.Front>self.Rear:
            print("The queue is empty now!")
        else:
            for k in range(self.Front,self.Rear+1):
                print(self.Array[k])




q=Queue(int(input("Enter size:")))
for k in range(5):
    data=input("Enter data:")
    q.EnqueuqElement(data)
print("The the Queue is:")
q.display()

q.ForntElement()

print("After dequeue the front element the queue is:")
q.DequeueEnlement()
q.DequeueEnlement()

q.display()

if q.EmptyOR_NoT():
    print("The Queue is empty!")
else:
    print("The Queue is not empty!")

if q.Full_Or_Not():
    print("The Queue is Full!")
else:
    print("The Queue is not Full!")

q.ForntElement()

q.EnqueuqElement(200)
q.display()
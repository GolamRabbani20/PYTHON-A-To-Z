class Circular_Queue_Using_Array:
    def __init__(self,size):
        self.Array=[]
        self.Size=size
        self.Front=-1
        self.Rear=-1

    def EnqueData(self,Item):
        if self.Front==-1 and self.Rear==-1:
            self.Front=0
            self.Rear=0
            self.Array.append(Item)

        elif (self.Rear+1)%self.Size==self.Front:
            print("The Queue is Overflow!")

        else:
            self.Rear=(self.Rear+1)%self.Size
            self.Array.append(Item)

    def DequeueData(self):
        if self.Front==-1 and self.Rear==-1:
            print("Underflow!")

        elif self.Rear==self.Front:
            self.Rear=-1
            self.Front=-1

        else:
            self.Front=(self.Front+1)%self.Size


    def display(self):
        if self.Front==-1 and self.Rear==-1:
            print("Empty!")
        else:
            temp=self.Front
            while temp!=self.Rear:
                print(self.Array[temp])
                temp=(temp+1)%self.Size
            print(self.Array[temp])

q=Circular_Queue_Using_Array(int(input("Enter size:")))
data=input("Enter data:").split()
for k in data:
    q.EnqueData(k)
print("The queue is:")
q.display()

while True:
    print("1.Enqueuing data")
    print("2.Dequeuing data")
    print("3.Display queue")
    print("0.Logout")
    chose=int(input("Chose your option:"))
    if chose is 1:
        data=input("Enter data:")
        q.EnqueData(data)
        print("After enqueuing data:")
        q.display()

    elif chose is 2:
        q.DequeueData()
        print("After Enqueuing data:")
        q.display()

    elif chose is 3:
        print("Final queue is:")
        q.display()

    elif chose is 0:
        print("Logging out...")
        break
    else:
        print("Invalid chose!")
class Implement_Queue_Using_Stack:
    def __init__(self,size):
        self.Stack1=[]
        self.Stack2=[]
        self.Size=size
        self.count=0
        self.Top1=-1
        self.Top2=-1

    def Push_In_Stack1(self,Item):
        if self.Top1==self.Size-1:
            print("Overflow!")

        else:
            self.count+=1
            self.Top1+=1
            self.Stack1.append(Item)

    def Pop_From_Stack1(self):
         if self.Top1==-1:
             print("Underflow!")

         else:
             self.Top1-=1
             return self.Stack1.pop()

    def Push_In_Stack2(self,Item2):
        if self.Top1==-1 and self.Top2==-1:
            print("The queue is empty!")

        else:
            self.Top2+=1
            self.Stack2.append(Item2)


    def Pop_From_Stack2(self):
        if self.Top2==-1:
            print("Underflow!")

        else:
            self.Top2-=1
            return self.Stack2.pop()

    def Behind_The_Seen(self):
        for k in range(self.count):
            Item2= self.Pop_From_Stack1()
            self.Push_In_Stack2(Item2)

        m = self.Pop_From_Stack2()
        print("The dequeue element is:", m)
        self.count -= 1
        for k in range(self.count):
            k = self.Pop_From_Stack2()
            self.Push_In_Stack1(k)

    def display(self):
        if self.Top1==-1:
            print("Empty!")

        else:
            print("Queue is:")
            temp = 0
            while temp<=self.Top1:
                print(self.Stack1[temp])
                temp+= 1
            print()

obj=Implement_Queue_Using_Stack(int(input("Enter size:")))
data=input("Enter data:").split()
for k in data:
    obj.Push_In_Stack1(k)

obj.Behind_The_Seen()
obj.Behind_The_Seen()
obj.display()



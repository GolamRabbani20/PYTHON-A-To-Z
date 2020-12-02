class Student:
    def __init__(self,roll):
        self.Roll=roll
        self.next=None

class Add_student:
    def __init__(self):
        self.head=None
        self.tail=None

    def Insert(self,Newst):
        if self.head is None:
            self.head=Newst
            self.tail=self.head
        else:
            self.tail.next=Newst
            self.tail=Newst

    def Rotate(self):
        temp1=self.head
        self.head=self.head.next
        temp1.next=None
        self.tail.next=temp1
        self.tail=self.tail.next

    def display(self):
        print(self.head.Roll,self.tail.Roll)

lst=Add_student()
x,y=input().split()
n=input().split()
for i in n:
    node=Student(int(i))
    lst.Insert(node)

for k in range(int(y)):
    lst.Rotate()

lst.display()

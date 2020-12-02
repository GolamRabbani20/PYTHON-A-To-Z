class CtreateNodes:
    def __init__(self,data):
        self.Data=data
        self.next=None

class CreateLinkLIst:
    def __init__(self):
        self.head=None

    def FirstInsertion(self,firstInsertionNode):
        tempNode=self.head
        self.head=firstInsertionNode
        self.head.next=tempNode
        del tempNode
    def LengthOfLinkedList(self):
        Lenght=0
        currentNode=self.head
        while currentNode is not None:
            currentNode=currentNode.next
            Lenght+=1
        return Lenght

    def MiddleInsertion(self,MiddleInsertionNode,position):
        currentNode=self.head
        previousNode=None
        currentPosition=0
        if self.LengthOfLinkedList()<=1:
            print("Sorry!Middle Insertion is not possible,Because there is less than 2 nods.")
        else:
            if position<=0 or position>=self.LengthOfLinkedList():
                print("Invalid Position!")
            while True:
                if currentPosition==position:
                    previousNode.next=MiddleInsertionNode
                    MiddleInsertionNode.next=currentNode
                    break
                previousNode=currentNode
                currentNode=currentNode.next
                currentPosition+=1


    def LastInsertion(self,LastInsertionNode):
        if self.head is None:
            self.head=LastInsertionNode
        else:
            startNode=self.head
            while startNode.next is not None:
                startNode=startNode.next
            startNode=LastInsertionNode


    def displayLinkedList(self):
        startNode=self.head
        while startNode is not None:
            print(startNode.Data,end=" ")
            startNode=startNode.next
        print()

lst=CreateLinkLIst()
while True:
    print("1.First Insertion.\n2.Middle Insertion.\n3.Last Insertion.\n4.Display Linked List.\n5.Exit.")
    n=int(input("Chose your Operation:"))
    print()


    if n is 1:
        ch=input("Do you want to insert first(Y/N):")
        if ch.upper()=="Y":
            n=int(input("Enter number of nodes:"))
            for i in range(n):
                data=input("Enter node's value:")
                node=CtreateNodes(data)
                lst.FirstInsertion(node)
            print()
        elif ch.upper() == 'N':
            print("The linked list after 1st insertion:",end=" ")
            lst.displayLinkedList()

        else:
            print("Invalid Chose!")

    elif n is 2:
        ch=input("Do you want to middle insertion(Y/N):")
        if ch.upper()=="Y":
            n=int(input("Enter number of nodes:"))
            while n>=1:
                data=input("Enter node's value:")
                position=int(input("Enter position where you want to insert:"))
                node=CtreateNodes(data)
                lst.MiddleInsertion(node,position)
                n-=1
            print()
        elif ch.upper()=="N":
            print("The linked list after middle insertion:",end=" ")
            lst.displayLinkedList()
        else:
            print("Invalid Chose!")

    elif n is 3:
        ch = input("Do you want to insert last?(Y/N):")
        if ch.upper() == "Y":
            n = int(input("Enter number of nodes:"))
            for i in range(n):
                data = input("Enter node's value:")
                node = CtreateNodes(data)
                lst.LastInsertion(node)
            print()
        elif ch.upper() == "N":
            print("The linked list after last insertion:", end=" ")
            lst.displayLinkedList()

        else:
            print("Invalid Chose!")

    elif n==4:
        if lst.LengthOfLinkedList()==0:
            print("The linked List is empty!")
        else:
            print("The Final Linked List is:",end=" ")
            lst.displayLinkedList()
    elif n==5:
         exit()
    else:
        print("Invalid Chose! Please try again.")

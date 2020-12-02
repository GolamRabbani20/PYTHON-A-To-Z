from math import ceil
class CreateNodes:
    def __init__(self,data):
        self.Data=data
        self.next=None

class Create_Singly_LinkedList:
    def __init__(self):
        self.head=None

    def CreateLinkedList(self,newNode):
        if self.head is None:
            self.head=newNode

        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=newNode

    def Check_The_List_Is_Empty_Or_Not(self):
        if self.head is None:
            return True
        else:
            return False

#Function-01
    def Insert_At_Begin_Of_The_LinkedList(self,NewNode):
        NewNode.next=self.head
        self.head=NewNode

#Function-02
    def Insert_After_Any_Position_Between_1st_And_Last_Node_Of_The_LinkedList(self,Position):
        if Position<=0 or Position>=self.Calculate_Length_Of_THe_LinkedList():
            print("Invalid position! Because there are less than 2 nodes.")

        else:
            CurrentPosition=1
            CurrentNode=self.head
            while CurrentPosition<Position:
                CurrentNode=CurrentNode.next
                CurrentPosition+=1
            newNode=CreateNodes(int(input("Enter data:")))
            newNode.next=CurrentNode.next
            CurrentNode.next=newNode

#Function-03
    def Insert_At_End_Of_The_LinkedList(self,newNode):
        Current=self.head
        while Current.next is not None:
            Current=Current.next
        Current.next=newNode

# Function-04
    def Delete_1st_Node_Of_The_LinkedList(self):
        Temp=self.head
        self.head=self.head.next
        del Temp

# Function-05
    def Delete_Any_Node_Between_1st_And_Last_Node_Of_The_LinkedList(self,Position):
        if Position<=1 or Position>=self.Calculate_Length_Of_THe_LinkedList():
            print("Invalid Position!")

        else:
            Current=self.head
            CurrentPosition=1
            while CurrentPosition<Position-1:
                Current=Current.next
                CurrentPosition+=1

            NextNode=Current.next
            Current.next=NextNode.next
            del NextNode

# Function-06
    def Delete_The_Last_Node_Of_The_LinkedList(self):
        Current=self.head
        PrevNode=None
        while Current.next is not None:
            PrevNode=Current
            Current=Current.next
        if Current==self.head:
            self.head=None

        else:
         PrevNode.next=None

        del Current

# Function-07
    def Calculate_Length_Of_THe_LinkedList(self):
        StartNode=self.head
        Length=0
        while StartNode is not None:
            StartNode=StartNode.next
            Length+=1
        return Length

# Function-08
    def Reverse_The_LinkedList(self):
        if self.head is None:
            return
        else:
            PrevNode=None
            NextNode=self.head
            CurrentNode=self.head
            while NextNode is not None:
                NextNode=CurrentNode.next
                CurrentNode.next=PrevNode
                PrevNode=CurrentNode
                CurrentNode=NextNode
            self.head=PrevNode

#Function-09
    def Reverse_1st_N_Nodes_Of_The_LinkedList(self,n):
        if n<=self.Calculate_Length_Of_THe_LinkedList():
                PrevNode = None
                NextNode = self.head
                CurrentNode = self.head
                for k in range(n):
                    NextNode = CurrentNode.next
                    CurrentNode.next = PrevNode
                    PrevNode = CurrentNode
                    CurrentNode = NextNode
                self.head.next=CurrentNode
                self.head = PrevNode
                print("After reversed Nth node the LinkedList:", end=" ")
                lst.Display_The_LinkedList()
        else:
            print("Number of nodes out of range!")


# Function-10
    def Find_The_Max_Node_Of_The_LinkedList(self):
        Max=self.head.Data
        StartNode = self.head.next
        while StartNode is not None:
            if StartNode.Data>Max:
                Max=StartNode.Data
            StartNode=StartNode.next
        print(Max)

#Function-11
    def Find_The_Min_Node_Of_The_LinkedList(self):
        Min=self.head.Data
        Current=self.head.next
        while Current is not None:
            if Current.Data<Min:
                Min=Current.Data
            Current=Current.next
        print(Min)

    # Function-12
    def Remove_Duplicates_From_The_LinkedList(List):
          print("Coming Soon!!!")

#Function-13
    def Search_a_Node_From_The_LinkedList(self,item):
        current=self.head
        x=[]
        pos=1
        while current is not None:
            if current.Data==item:
              x.append(pos)
            current=current.next
            pos+=1
        return x


#Function-14
    def Count_The_Number_Of_Occurrences_Of_an_Element_in_the_LinkedList(self,item):
        current=self.head
        count=0
        while current:
            if current.Data==item:
                count+=1
            current=current.next
        return count

#Function-15
    def Find_Number_of_Occurrences_of_All_Elements_in_a_LinkedList(self):
        print("Coming Soon!!!")

#Function-16
    def Print_Middle_most_Node_of_a_LinkedList(self):
        current=self.head
        Len=self.Calculate_Length_Of_THe_LinkedList()
        if Len%2:
            Len=ceil(Len/2)
            for k in range(1,Len+1):
                if k==Len:
                    print("There is one middle most element in the LinkedLIst that is ",current.Data)
                current = current.next

        else:
            Len=Len//2
            for k in range(1,Len+1): #1 2 3 4 5
                if k==Len:
                   print("There are 2 middle most elements {} and {}".format(current.Data,current.next.Data))
                current=current.next


#Function-17
    def Print_The_Alternate_Nodes_in_a_LinkedList(self):
        current=self.head
        while current:
            print(current.Data,end=" ")
            current=current.next.next

#Function-18
    def Display_The_LinkedList(self):
        CurrentNode=self.head
        while CurrentNode is not None:
            print(CurrentNode.Data,end=" ")
            CurrentNode=CurrentNode.next
        print()

#======================================================================================================================================
#======================================================================================================================================
lst=Create_Singly_LinkedList()

while True:
    chose=input("Do you want to (Press any character for exit) Create LinkedList(Y/N):")
    if chose.upper()=="Y":
        data=input("Enter data for linkedList:").split()
        for k in data:
            node=CreateNodes(int(k))
            lst.CreateLinkedList(node)
        print("The created linked list:",end=" ")
        lst.Display_The_LinkedList()
        print()

    elif chose.upper()=="N":
        while True:
            if lst.Check_The_List_Is_Empty_Or_Not() is False:
                print("Please,Chose an option")
                print("...........................................")
                print("1.Insert at begin")
                print("2.Insert after any position")
                print("3.Insert at end")
                print("4.Delete first node")
                print("5.Delete any node between 1st & last node")
                print("6.Delete last node")
                print("7.Length")
                print("8.Reverse")
                print("9.Reverse_1st_N_Nodes")
                print("10.Maximum")
                print("11.Minimum")
                print("12.Remove duplicate nodes")
                print("13.Search a node")
                print("14.Count The Number Of Occurrences Of an Element")
                print("15.Find Number of Occurrences of All Elements")
                print("16.Print Middle most Node")
                print("17.Print The Alternate Nodes")
                print("18.Function of two LinkedList")
                print("19.Display")
                print("20.Exit")
                chose = int(input("Enter your chose:"))
                print()

                if chose is 1:
                    while True:
                        chose=input("Do you want to insert at begin(Y/N):")
                        print()
                        if chose.upper()=="Y":
                            node=CreateNodes(int(input("Enter a data:")))
                            lst.Insert_At_Begin_Of_The_LinkedList(node)

                        elif chose.upper()=="N":
                            print("After Insert at begin of the LinkedList:",end=" ")
                            lst.Display_The_LinkedList()
                            break

                elif chose is 2:
                    while True:
                        chose = input("Do you want to insert after given position(Y/N):")
                        print()
                        if chose.upper() == "Y":
                            position = int(input("Enter a position:"))
                            lst.Insert_After_Any_Position_Between_1st_And_Last_Node_Of_The_LinkedList(position)
                            print("After insert  position {} the LinkedList:".format(position), end=" ")
                            lst.Display_The_LinkedList()

                        elif chose.upper() == "N":
                            break
                        else:
                            print("Invalid chose!")

                elif chose is 3:
                    while True:
                        chose = input("Do you want to insert at End(Y/N):")
                        print()
                        if chose.upper() == "Y":
                            node = CreateNodes(int(input("Enter a data:")))
                            lst.Insert_At_End_Of_The_LinkedList(node)
                        elif chose.upper() == "N":
                            print("After Insert at end of the LinkedList:", end=" ")
                            lst.Display_The_LinkedList()
                            break

                elif chose is 4:
                    while True:
                        chose = input("Do you want to delete 1st node(Y/N):")
                        if lst.Calculate_Length_Of_THe_LinkedList():
                            if chose.upper()=='Y':
                                print("After deleting 1st node:",end=" ")
                                lst.Delete_1st_Node_Of_The_LinkedList()
                                lst.Display_The_LinkedList()
                                print()
                            elif chose.upper() =='N':
                                break
                        else:
                            print("The List is empty now!.Deletion is not possible.")
                            break

                elif chose is 5:
                    while True:
                        chose = input("Do you want to delete at specific node(Y/N):")
                        if chose.upper()=='Y':
                            position=int(input("Enter Deleting position:"))
                            lst.Delete_Any_Node_Between_1st_And_Last_Node_Of_The_LinkedList(position)
                            print("After deleting {} position's node:".format(position),end=" ")
                            lst.Display_The_LinkedList()
                            print()

                        elif chose.upper() =='N':
                            break

                elif chose is 6:
                    while True:
                        chose = input("Do you want to delete last node(Y/N):")
                        if lst.Calculate_Length_Of_THe_LinkedList():
                            if chose.upper() == 'Y':
                                print("After deleting the last node:",end=" ")
                                lst.Delete_1st_Node_Of_The_LinkedList()
                                lst.Display_The_LinkedList()
                                print()

                            elif chose.upper()=='N':
                                break
                        else:
                            print("The List is empty now!.Deletion is not possible.")
                            break

                elif chose is 7:
                    print("Length of the LinkedList:",lst.Calculate_Length_Of_THe_LinkedList(),end=" ")
                    print()

                elif chose is 8:
                    print("After reversed the LinkedList:",end=" ")
                    lst.Reverse_The_LinkedList()
                    lst.Display_The_LinkedList()
                    print()

                elif chose is 9:
                    n=int(input("Enter Nth node:"))
                    lst.Reverse_1st_N_Nodes_Of_The_LinkedList(n)

                elif chose is 10:
                    print("The Maximum value in the LinkedList:",end=" ")
                    lst.Find_The_Max_Node_Of_The_LinkedList()

                elif chose is 11:
                    print("The Minimum value in the LinkedList:", end=" ")
                    lst.Find_The_Min_Node_Of_The_LinkedList()

                elif chose is 12:
                    lst.Remove_Duplicates_From_The_LinkedList()

                elif chose is 13:
                    while True:
                        chose=input("Do you want to search item(Y/N):")
                        if chose.upper()=="Y":
                            item=int(input("Enter search item:"))
                            x=lst.Search_a_Node_From_The_LinkedList(item)
                            if x:
                              print(item,"is found at position {}:".format(x))
                            else:
                                print(item,"is not present is the LinkedList.")

                        elif chose.upper()=="N":
                            break
                        else:
                            print("Invalid chose!")
                            break

                elif chose is 14:
                    while True:
                        chose = input("Do you want to Count The Number Of Occurrences Of an Element in the LinkedList(Y/N):")
                        if chose.upper() == "Y":
                            item = int(input("Enter item:"))
                            n=lst.Count_The_Number_Of_Occurrences_Of_an_Element_in_the_LinkedList(item)
                            print("The_Number_Of_Occurrences_Of Element {} in_the_LinkedList:".format(item),n)

                        elif chose.upper() == "N":
                            break
                        else:
                            print("Invalid chose!")

                elif chose is 15:
                    lst.Find_Number_of_Occurrences_of_All_Elements_in_a_LinkedList()

                elif chose is 16:
                    lst.Print_Middle_most_Node_of_a_LinkedList()

                elif chose is 17:
                    print("The Alternate nodes of the LinkedList:",end=" ")
                    lst.Print_The_Alternate_Nodes_in_a_LinkedList()
                    print()

                elif chose is 18:
                    pass

                elif chose is 19:
                    print("The final LinkedList is:",end=" ")
                    lst.Display_The_LinkedList()

                elif chose is 20:
                    break

                else:
                    print("Invalid Chose!")
            else:
                print("The List is Empty! Please,Create a list first.\n")
                break

    else:
        print("Invalid Chose!")
        break
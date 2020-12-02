class CreateNodes:
    def __init__(self, data):
        self.Data = data
        self.next = None


class CreateLinkedList:
    def __init__(self):
        self.head = None

    def Calculate_Length(self):
         CurrentNode=self.head
         Length=0
         while CurrentNode is not None:
             CurrentNode=CurrentNode.next
             Length+=1
         return Length

    def Check_Empty_Or_Not(self):
        if self.head is None:
            return True
        else:
            return False

    def CreateLinkedList(self,newNode):
        if self.head is None:
            self.head = newNode

        else:
            LastNode = self.head
            while LastNode.next is not None:
                LastNode = LastNode.next
            LastNode.next = newNode


    def FirstInsertion(self,newNode):
            TempNode=self.head
            self.head=newNode
            self.head.next=TempNode
            del TempNode

    def Middle_Insertion(self,NewNode,Position):
        CurrentNode = self.head
        CurrentPosition = 0
        PreviousNode = None
        if self.Calculate_Length() > 1:
            if Position > 0 and Position < self.Calculate_Length():
                while CurrentNode is not None:
                    if Position == CurrentPosition:
                        PreviousNode.next = NewNode
                        NewNode.next = CurrentNode
                        break
                    PreviousNode = CurrentNode
                    CurrentNode = CurrentNode.next
                    CurrentPosition += 1

    def Last_Insertion(self,newNode):
        StartNode=self.head
        PreviousNode=None
        while StartNode is not None:
            PreviousNode = StartNode
            StartNode = StartNode.next
        PreviousNode.next=newNode
        newNode.next=None



    def Firest_Deletion(self):
        CurrentNode = self.head
        self.head=CurrentNode.next
        del CurrentNode

    def Middle_Deletion(self,Position):
        StartNode=self.head
        CurrentPosition=1
        PreviousNode=None
        while StartNode.next is not None:
            if Position==CurrentPosition:
                PreviousNode.next=StartNode.next
                del StartNode
                break

            PreviousNode=StartNode
            StartNode=StartNode.next
            CurrentPosition+=1

    def Last_Deletion(self):
        CurrentNode=self.head
        PreviousNode=None
        if self.Calculate_Length()>1:
            while CurrentNode.next is not None:
                 PreviousNode=CurrentNode
                 CurrentNode=CurrentNode.next
            PreviousNode.next=CurrentNode.next
            del CurrentNode
        else:
            self.head=None
            del CurrentNode

    def Delete_Any_Node_By_Position(self,Position):
        if Position==1:
            CurrentNode=self.head
            self.head=CurrentNode.next
            del CurrentNode

        elif Position==self.Calculate_Length():
            self.Last_Deletion()

        elif Position>1 and Position<self.Calculate_Length():
            CurrentNode = self.head
            CurrentPosition = 1
            PreviousNode = None
            while CurrentNode.next is not None:
                if Position == CurrentPosition:
                    PreviousNode.next = CurrentNode.next
                    del CurrentNode
                    break
                PreviousNode = CurrentNode
                CurrentNode = CurrentNode.next
                CurrentPosition += 1

    def Delete_Any_Node_By_value(self,NodeData):
        StartNode = self.head
        PreviousNode = None
        if self.head.Data==NodeData:
            self.head=StartNode.next
            del StartNode.Data
        else:
          while StartNode.next is not None:
            if StartNode.Data == NodeData:
                PreviousNode.next = StartNode.next
                del StartNode.Data
                break

            PreviousNode = StartNode
            StartNode = StartNode.next

          else:
             PreviousNode.next=None


    def Display_Linked_List(self):
        CurrentNode=self.head
        while CurrentNode is not None:
            print(CurrentNode.Data,end=" ")
            CurrentNode=CurrentNode.next
        print()
#...................................................................................................................
#..................................................................................................................
lst=CreateLinkedList()
while True:
 try:
   print("1.Create Linked list.")
   print("2.Insertion.")
   print("3.Deletion.")
   print("4.Show final list.")
   print("5.Exit.")
   option=int(input("Chose your option:"))
   print()
   #First Insertion
   if option is 1:
       n=int(input("Enter number of node:"))
       for i in range(n):
           data=input("Enter node's data:")
           node=CreateNodes(data)
           lst.CreateLinkedList(node)
       print("The created list is:",end=" ")
       lst.Display_Linked_List()
       print()

   if option is 2:
       print("You have chosen Insertion.")
       while True:
           print("1.First Insertion.")
           print("2.Middle Insertion.")
           print("3.Last Insertion")
           print("4.Exit.")
           n=int(input("Chose your insertion option:"))
           print()

           if n is 1:
               number_of_node=int(input("Enter number of nodes:"))
               for k in range(number_of_node):
                   data=input("Enter value of node-"+str(k+1)+":")
                   node=CreateNodes(data)
                   lst.FirstInsertion(node)
               print("After first insertion:", end=" ")
               lst.Display_Linked_List()
               print()

            #Middle Insertion
           elif n is 2:
               if lst.Check_Empty_Or_Not() is True:
                   print("Sorry! The list is empty.")

               else:
                   if lst.Calculate_Length() >= 2:
                       number_of_node=int(input("Enter number of nodes:"))
                       for k in range(number_of_node):
                               data=input("Enter value of node-"+str(k+1)+":")
                               position = int(input("Enter after which position:"))
                               if position>=1 and position<lst.Calculate_Length():
                                   node=CreateNodes(data)
                                   print("After inserting at position_"+str(position)+":", end=" ")
                                   lst.Middle_Insertion(node,position)
                                   lst.Display_Linked_List()
                               else:
                                   print("Invalid position!")
                   else:
                       print("Sorry! Middle insertion is not possible,Because there is less than 2 nodes.")

               print()

           #Last Insertion
           elif n is 3:
               if lst.Check_Empty_Or_Not() is True:
                   print("Empty! Last Insertion is not possible.")
               else:
                   number_of_node=int(input("Enter number of nodes:"))
                   for k in range(number_of_node):
                       data=input("Enter value of node-"+str(k+1)+":")
                       node=CreateNodes(data)
                       print("After last insertion:", end=" ")
                       lst.Last_Insertion(node)
                       lst.Display_Linked_List()
                   print()

           elif n is 4:
               break

           else:
               print("Invalid chose! Please try again.")

   elif option is 3:
       while True:
           print("1.First deletion.")
           print("2.Middle deletion")
           print("3.Last deletion.")
           print("4.Delete any node.")
           print("5.Exit.")
           chose=int(input("Chose your option:"))
           print()

           #First deletion
           if chose is 1:
               if lst.Check_Empty_Or_Not() is True:
                   print("Sorry! The list is empty.")
               else:
                   lst.Firest_Deletion()
                   print("After first deletion:", end=" ")
                   lst.Display_Linked_List()
                   print()
           #Middle deletion
           elif chose is 2:
               if lst.Check_Empty_Or_Not() is True:
                   print("Sorry! The list is empty.")
               else:
                   if lst.Calculate_Length() > 2:
                       position=int(input("Enter position:"))
                       if position>1 and position<lst.Calculate_Length():
                           lst.Middle_Deletion(position)
                           print("After middle deletion:",end=" ")
                           lst.Display_Linked_List()
                           print()
                       else:
                           print("Invalid position!")
                   else:
                       print("Sorry! Middle deletion is not possible,Because there is less than 3 nodes.")
           #last deletion
           elif chose is 3:
               if lst.Check_Empty_Or_Not() is True:
                   print("Sorry! The list is empty.")
               else:
                   lst.Last_Deletion()
                   print("After last deletion:", end=" ")
                   lst.Display_Linked_List()
                   print()

           #Delete any node
           elif chose is 4:
               print("1.Delete any node by position.")
               print("2.Delete any node by node's value.")
               chose=int(input("Chose your option:"))
               print()
               #By Position
               if chose is 1:
                   if lst.Check_Empty_Or_Not() is True:
                       print("Sorry! The list is empty.")

                   else:
                       position=int(input("Enter position:"))
                       print("After deleting the certain node(Position):",end=" ")
                       lst.Delete_Any_Node_By_Position(position)
                       lst.Display_Linked_List()
                       print()
               #By Value
               elif chose is 2:
                   if lst.Check_Empty_Or_Not() is True:
                       print("Sorry! The list is empty.")

                   else:
                       value = input("Enter node's value:")
                       print("After deleting the certain node(Value):", end=" ")
                       lst.Delete_Any_Node_By_value(value)
                       lst.Display_Linked_List()
                       print()

               else:
                   print("Invalid chose!")


           elif chose is 5:
               break

           else:
               print("Invalid chose! Please try again.")

   elif option is 4:
       if lst.Check_Empty_Or_Not() is True:
           print("The final list is empty.")

       else:
           print("The final list is:",end=" ")
           lst.Display_Linked_List()

   elif option is 5:
       exit()

   else:
       print("You hove chosen invalid option!")
 except ValueError:
     print("Error!\n")
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

    def Insert_At_Begin_Of_The_LinkedList(self):
        pass

    def Insert_After_Any_Position_Between_1st_And_Last_Node_Of_The_LinkedList(self):
        pass

    def Insert_At_End_Of_The_LinkedList(self):
        pass

    def Delete_1st_Node_Of_The_LinkedList(self):
        pass

    def Delete_Any_Node_Between_1st_And_Last_Node_Of_The_LinkedList(self):
        pass

    def Delete_The_Last_Node_Of_The_LinkedList(self):
        pass

    def Calculate_Length_Of_THe_LinkedList(self):
        pass

    def Check_The_List_Is_Empty_Or_Not(self):
        pass

    def Reverse_The_LinkedList(self):
        pass

    def Reverse_1st_N_Nodes_Of_The_LinkedList(self):
        pass

    def Find_The_Max_Node_Of_The_LinkedList(self):
        pass

    def Find_The_Min_Node_Of_The_LinkedList(self):
        pass

    def Remove_Duplicates_From_The_LinkedList(self):
        pass

    def Search_a_Node_From_The_LinkedList(self):
        pass

    def Count_The_Number_Of_Occurrences_Of_an_Element_in_the_LinkedList(self):
        pass

    def Find_Number_of_Occurrences_of_All_Elements_in_a_LinkedList(self):
        pass

    def Print_Middle_most_Node_of_a_LinkedList(self):
        pass

    def Print_The_Alternate_Nodes_in_a_LinkedList(self):
        pass

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
    print("Please,Chose an option")
    print("...........................................")
    print("1.Create LinkedList")
    print("2.Insert at begin")
    print("3.Insert after any position")
    print("4.Insert at end")
    print("5.Delete first node")
    print("6.Delete any node between 1st & last node")
    print("7.Delete last node")
    print("8.Length")
    print("9.Reverse")
    print("10.Reverse_1st_N_Nodes")
    print("11.Maximum")
    print("12.Minimum")
    print("13.Remove duplicate nodes")
    print("14.Search a node")
    print("15.Count The Number Of Occurrences Of an Element")
    print("16.Find Number of Occurrences of All Elements")
    print("17.Print Middle most Node")
    print("18.Print The Alternate Nodes")
    print("20.Function of two LinkedList")
    print("19.Display")
    chose=int(input("Enter your chose:"))
    print()

    if chose is 1:
        data=input("Enter data for linkedList:").split()
        for k in data:
            node=CreateNodes(k)
            lst.CreateLinkedList(node)
        print("The created linked list:",end=" ")
        lst.Display_The_LinkedList()
        print()
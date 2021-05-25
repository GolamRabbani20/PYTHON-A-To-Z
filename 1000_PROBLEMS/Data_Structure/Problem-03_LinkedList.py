#Python Program to Search for an Element in the Linked List using Recursion
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def InsertNode(self,NewNode):
        if self.head is None:
            self.head=NewNode
        else:
            LastNode=self.head
            while LastNode.next is not None:
                LastNode=LastNode.next
            LastNode.next=NewNode

    def SearchItem(self,item):
        return self.Index_Finder(item,0,self.head)

    def Index_Finder(self,Item,Index,currentNode):
        if currentNode is None:
            return -1
        if currentNode.Data==Item:
            return Index
        else:
            return self.Index_Finder(item,Index+1,currentNode.next)


    def display(self):
        currentNode=self.head
        while currentNode!=None:
            print(currentNode.Data,end=" ")
            currentNode=currentNode.next
        print()


lst=LinkedList()
n=int(input("Enter number of nodes:"))
for k in range(n):
    data=input("Enter value:")
    node=Node(data)
    lst.InsertNode(node)

print("The linked List is:",end=" ")
lst.display()

item=input("Enter a item:")
result=lst.SearchItem(item)
if result==-1:
    print(item,"is not found at index.")
else:
    print(item,"is found at index",result)

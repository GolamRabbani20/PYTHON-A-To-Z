import random
class Node:
    def __init__(self,data):
        self.Data=data
        self.Left=None
        self.Right=None

class BTree:
    def Create(self):
        data=int(input("Enter data(-1 for no node):"))
        if data==1:
            return 0
        else:
            newNode=Node(data)

        print("Left child of "+str(data)+":")
        newNode.Left=self.Create()
        print("Right child of " + str(data) + ":")
        newNode.Right = self.Create()
        return newNode

    def PreOrder(self,root):
        if root==0:
            return
        print(root.Data,end=" ")
        self.PreOrder(root.Left)
        self.PreOrder(root.Right)

    def InOrder(self,root):
        if root == 0:
            return

        self.InOrder(root.Left)
        print(root.Data, end=" ")
        self.InOrder(root.Right)


    def PostOrder(self,root):
        if root==0:
            return
        self.PostOrder(root.Left)
        self.PostOrder(root.Right)
        print(root.Data, end=" ")


Btr=BTree()
root=Btr.Create()
print("Pre_order is:",end=" ")
Btr.PreOrder(root)
print()

print("In_order is:",end=" ")
Btr.InOrder(root)
print()

print("Post_order is:",end=" ")
Btr.PostOrder(root)
print()
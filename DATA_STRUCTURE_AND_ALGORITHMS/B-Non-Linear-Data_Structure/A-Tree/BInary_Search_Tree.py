class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def CreateTree(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self._CreateTree(data,self.root)

    def _CreateTree(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left==None:
                cur_node.left=Node(data)
            else:
                self._CreateTree(data,cur_node.left)
        elif data>cur_node.data:
            if cur_node.right==None:
                cur_node.right=Node(data)
            else:
                self._CreateTree(data,cur_node.right)

        else:
            print("The node is already present in the tree.")

    def dis(self):
        self.PreOrder(self.root)

    def PreOrder(self,root):
        if self.root==None:
            return
        print(self.root.data,end=" ")
        self.PreOrder(self.root.left)
        self.PreOrder(self.root.right)

My_BST=BST()
while True:
    ch=input("Do you want to insert node(Y/N):")
    if ch.upper()=="Y":
        data = int(input("Enter data:"))
        My_BST.CreateTree(data)

    else:
        My_BST.dis()
        break
class Node:
    def __init__(self,data):
        self.Data=data
        self.left=None
        self.right=None

class Insert_Node_At_BST:
    def __init__(self):
       self.root=None
    def CreateNode(self,NewNode):
        if self.root==None:
            self.root=NewNode
        else:
            if self.root.Data<NewNode.Data:
                self.root.left=NewNode
            else:
                self.root.right=NewNode

bst=Insert_Node_At_BST()
for k in range(3):
    data=int(input("Enter node data:"))
    bst.CreateNode(Node(data))
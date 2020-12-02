class BSTNode:
    def __init__(self,data):
        self.Data=data
        self.left=None
        self.right=None

    def InsertNoder_at_BST(self,val):
        if self.Data==val:
            return
        elif self.Data<val:
            if self.right==None:
                self.right=BSTNode(val)
            else:
                self.right.InsertNoder_at_BST(val)


        else:
            if self.left is None:
                self.left=BSTNode(val)
            else:
                self.left.InsertNoder_at_BST(val)

import  random
My_BST=BSTNode(int(input("Enter root node:")))
for i in range(20):
    My_BST.InsertNoder_at_BST(random.randint(0,100))
#My_BST.PreOrder(My_BST)





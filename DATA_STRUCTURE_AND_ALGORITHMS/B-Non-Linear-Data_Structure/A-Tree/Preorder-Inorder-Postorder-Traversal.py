class Node:
    def __init__(self,data):
        self.Data=data
        self.Left=None
        self.Right=None

class BTree:
    def Create(self):
        data=int(input("Enter data(-1 for no node):"))
        if data==-1:
            return 0
        else:
            newNode=Node(data)

        print("Left child of "+str(data)+":")
        newNode.Left=self.Create()
        print("Right child of " + str(data) + ":")
        newNode.Right = self.Create()
        return newNode

def PreOrder(root):
    if root==0:
        return
    print(root.Data,end=" ")
    PreOrder(root.Left)
    PreOrder(root.Right)

def InOrder(root):
    if root == 0:
        return

    InOrder(root.Left)
    print(root.Data, end=" ")
    InOrder(root.Right)


def PostOrder(root):
    if root==0:
        return
    PostOrder(root.Left)
    PostOrder(root.Right)
    print(root.Data, end=" ")


Btrees=BTree()
root=Btrees.Create()
print("Preorder is:",end=" ")
PreOrder(root)
print()


print("Inorder is:",end=" ")
InOrder(root)
print()

print("Postorder is:",end=" ")
PostOrder(root)
print()
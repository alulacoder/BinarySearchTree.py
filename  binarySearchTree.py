class Treenode:
    def __init__(self, x):
        self.leftchild = None
        self.rightchild = None
        self.data = x

    
def InorderTraversal(root):
        if root is not None:    
            if root.leftchild is not None:
                InorderTraversal(root.leftchild)
            print(root.data)
            if root.rightchild is not None:
                InorderTraversal(root.rightchild)

    
def Insert(root, k):
        if root is None:
                return Treenode(k)
        if root.data < k:
              root.rightchild = Insert(root.rightchild, k)
        else:
              root.leftchild = Insert(root.leftchild, k)
        return root

def Search(root, k):
        if root.data == k:
            return root.data
        elif root.data > k and root.leftchild is not None:
            return Search(root.leftchild, k)
        elif root.data < k and root.leftchild is None:
            return Search(root.rightchild, k)
        else:
            return -1
        
n = int(input("Enter the number of elements you want in the tree - "))
root = None
for i in range(n):
    x = int(input ("Enter the node value - "))
    root = Insert(root, x)

InorderTraversal(root)

key = int(input("Enter the key to be searched- "))
keyNode = Search(root, key)

if keyNode == -1:
    print("Key does not exist in the tree")
else:
    print("Key exists", keyNode.data)
        
        
        
              
         
        
             

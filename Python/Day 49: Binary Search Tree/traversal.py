class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data, sep = " ")
        inorderTraversal(root.right)
        
def preorderTraversal(root):
    if root:
        print(root.data, sep = " ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)
        
def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data, sep = " ")
        
r = Node(20)
r.left = Node(10)
r.right = Node(30)
r.left.left = Node(5)      
r.left.right = Node(15)
r.right.left = Node(25)      
r.right.right = Node(35)

inorderTraversal(r)
preorderTraversal(r)
postorderTraversal(r)

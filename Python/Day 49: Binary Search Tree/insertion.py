# Implement a binary search tree.

#Insertion
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def insertion(root, key):
    if root is None:
        return Node(key)
    if root.value == key:
        return root
    elif root.value < key:
        root.right = insertion(root.right, key)
    else:
        root.left = insertion(root.left, key)
    return root
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, sep = " ")
        inorder(root.right)
        
r = Node(15)
r = insertion(r, 10)
r = insertion(r, 8)
r = insertion(r, 12)
r = insertion(r, 18)
inorder(r)

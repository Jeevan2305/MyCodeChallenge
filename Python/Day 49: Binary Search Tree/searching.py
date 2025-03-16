#Day 49: Binary Search Tree

#Searching
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.right, key)
    return search(root.left, key)
        
r = Node(20)
r.left = Node(10)
r.right = Node(30)
r.left.left = Node(5)      
r.left.right = Node(15)
r.right.left = Node(25)      
r.right.right = Node(35)

print("Found" if search(r, 25) else "Not Found")
print("Found" if search(r, 40) else "Not Found")

# Deletion 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current.data

    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current.data

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # Node with only one child or no child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            # Node with two children: Get the inorder successor
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

if __name__ == "__main__":
    r = Node(20)
    r.left = Node(10)
    r.right = Node(30)
    r.left.left = Node(5)
    r.left.right = Node(15)
    r.right.left = Node(25)
    r.right.right = Node(35)

    r.inorder()
    print("-----")
    r.delete(5)
    r.inorder()
    print("-----")
    r.delete(15)
    r.inorder()
    print("-----")
    r.delete(30)
    r.inorder()

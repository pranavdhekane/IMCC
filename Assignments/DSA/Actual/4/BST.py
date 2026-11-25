class Node:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data):
        node = Node(data)

        if self.root is None:
            self.root = node
            return

        temp = self.root
        while True:
            if node.data < temp.data:
                if temp.left is None:
                    temp.left = node
                    return 

                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = node
                    return 
                else:
                    temp = temp.right

    def search(self, productID):
        temp = self.root

        while temp:
            if temp.data == productID:
                return True
            elif temp.data < productID:
                temp = temp.right
            else:
                temp = temp.left

        return False

    def delete(self, rt, value):
        if rt is None:
            return None

        if value < rt.data:
            rt.left = self.delete(rt.left, value)
        elif value > rt.data:
            rt.right = self.delete(rt.right, value)
        else:
            if rt.left is None:
                return rt.right

            if rt.right is None:
                return rt.left

            temp = rt.right
            while temp.left:
                temp = temp.left

            rt.data = temp.data
            rt.right = self.delete(rt.right, temp.data)

        return rt
    
    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return

        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")

    def minimum(self):
        if self.root is None:
            print("No data in Tree")
            return None
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp.data

    def maxmium(self):
        if self.root is None:
            print("No data in Tree")
            return None
        temp = self.root
        while temp.right:
            temp = temp.right
        return temp.data

    
productIdTree = BST()
print("######### 1 #########")
l = [150, 100, 200, 75, 125, 175, 250, 60, 90, 110]
for i in l:
    productIdTree.insert(i)
print("Inserted..")
print()

print("######### 2 #########")
print("Product ids in ascending order: ")
productIdTree.inorder(productIdTree.root)
print()
print()

print("######### 3 #########")
print("175 id is Present" if productIdTree.search(175) else "175 id not present")
print()

print("######### 4 #########")
print("100 id is Present" if productIdTree.search(100) else "100 id not present")
print("Deleting Product id 100")
productIdTree.root = productIdTree.delete(productIdTree.root, 100)
print("100 id is Present" if productIdTree.search(100) else "100 id not present")
print()

print("######### 5 #########")
print("Inorder Traversal: ")
productIdTree.inorder(productIdTree.root)
print()

print("Preorder Traversal: ")
productIdTree.preorder(productIdTree.root)
print()

print("Postorder Traversal: ")
productIdTree.postorder(productIdTree.root)
print()
print()

print("######### 6 #########")
print("Minimum Product ID: ", productIdTree.minimum())

print("Maximum Product ID: ", productIdTree.maxmium())
print()
print()

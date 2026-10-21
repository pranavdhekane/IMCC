class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = newNode

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)

    def insertPos(self, pos, data):
        n = 0
        temp = self.head

        newNode = Node(data)

        if pos == 0:
            newNode.next = self.head
            self.head = newNode
            return

        for i in range(pos-1):
            if temp is None:
                print("Invalid Index")
                return

            temp = temp.next

        if temp is None:
            print("Invlaid Index")
            return

        newNode.next = temp.next
        temp.next = newNode

    def deleteNegative(self):

        while self.head and self.head.data < 0:
            self.head = self.head.next

        if self.head is None:
            return

        prev = self.head
        temp = prev.next
        while temp:
            if temp.data < 0:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
                

##### Questions #####

ll = LinkedList()

# 1. append
print("##### Q1 #####")
n = int(input("Enter number of nodes: "))
for i in range(n):
    print("Enter node ", i, end=": ")
    ll.append(int(input()))


# 2. Traverse
print("\n##### Q2 #####")
print("Traversing the LinkedList: ")
ll.traverse()

# 3. insert at position
print("\n##### Q3 #####")
pos = int(input("Enter pos: "))
data = int(input("Enter data: "))
ll.insertPos(pos, data)
ll.traverse()

# 4. delete negative Node
print("\n##### Q4 #####")
ll.deleteNegative()
ll.traverse()
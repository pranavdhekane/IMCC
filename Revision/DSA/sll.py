class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert(self, data, pos):
        "insert at a any position (zero indexed)"
        new_node = Node(data)
        temp = self.head

        if pos == 0:
            self.prepend(val)
            return
        
        for i in range(1, pos):
            if not temp:
                print("Invalid Position")
                return
            temp = temp.next

        if not temp:
            print("Invalid Position")
            return
        new_node.next = temp.next
        temp.next = new_node

    def delete(self, value):
        prev = None
        curr = self.head

        if not self.head:
            print("Empty list")
            return

        if curr.data == value:
            self.head = self.head.next
            return

        while curr:
            if curr.data == value:
                prev.next = curr.next
                return
            else:
                prev = curr
                curr = curr.next 
        else:
            print("no element found")
            return

    def search(self, value):
        temp = self.head
        pos = 0
        while temp:
            if temp.data == value:
                print(f"{value} found at {pos}th node")
                return
            pos += 1
            temp = temp.next
        else:
            print("Not present")

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")


linkedlist = SLL()
while True:
    print()
    print("1. append")
    print("2. prepend")
    print("3. insert")
    print("4. delete")
    print("5. search")
    print("6. print list")
    print("exit")

    n = int(input())
    if n < 6:
        val = int(input("Enter value "))

        if n == 1:
            linkedlist.append(val)
        elif n == 2:
            linkedlist.prepend(val)
        elif n == 3:
            print("Insert position ")
            pos = int(input())
            linkedlist.insert(val, pos)
        elif n == 4:
            linkedlist.delete(val)
        else:
            linkedlist.search(val)
    elif n == 6:
        linkedlist.print_list()
    else:
        break
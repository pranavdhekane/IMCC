class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        
    def insert(self, data, position):
        new_node = Node(data)

        temp = self.head
        for i in range(0, position):
            if temp is None:
                print("invalid position")
                return
            temp = temp.next

        if temp is None:
            print("invlaid posisiton")
            return

        new_node.next = temp.next
        temp.prev.next = new_node

    def delete(self, value):
        if self.head.data == value:
            if self.head.next is None:
                self.head = None
            else:
                self.head.next.prev = self.head.prev

        temp = self.head
        while temp:
            if temp.data == value:
                temp.prev = temp.next
                return
            
        print("no element found")

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

        print("None")

    def display_backward(self):
        temp = self.head
        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end="->")
            temp = temp.prev
        print("None")
        return


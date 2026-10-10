class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter number of Nodes: "))
        for i in range(n):
            data = int(input(f"Enter values of {i}th Node: "))
            self.insert(data)

    def insert(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = node

    def insert_idx(self, data, idx):
        node = Node(data)

        if idx < 0:
            print("Enter valid index")
            return
        
        if idx == 0:
            node.next = self.head
            self.head = node
            return

        temp = self.head

        for i in range(idx-1): # [0, 1, 2, 3]
            if temp is None:
                print("idx is more than size of linkedlist")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        node.next = temp.next
        temp.next = node


    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> " )
            temp = temp.next

        print("None")

    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if slow:
            print(slow.data)
        else:
            print("list is empty")

    def delete(self, idx):
        if self.head is None:
            print("list is empty")
            return 

        if idx < 0:
            print("Enter valid idx")
            return 

        if idx == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(idx - 1):
            if temp.next is None:
                print("Invalid index : ")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid Position")
            return

        temp.next = temp.next.next


    def reverse(self):
        prev = None
        current = self.head

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        self.head = prev

    def pair_sum(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data, " -> ", temp.next.data, "\nsum : ", temp.data + temp.next.data)
            temp = temp.next



def main():
    ll = LinkedList()

    print("####### 1. Create a LinkedList #######")
    ll.create()
    
    print("\n###### 2. Traverse a LinkedList #######")
    ll.traverse()

    print("\n####### 3. Insert at random position #######")
    idx = int(input("Enter position: "))
    data = int(input("Enter data: "))
    ll.insert_idx(data, idx)
    ll.traverse()

    print("\n####### 4. Middle of List #######")
    ll.middle()

    print("\n####### 5. Delete Node #######")
    idx = int(input("Enter position: "))
    ll.delete(idx)
    ll.traverse()

    print("\n####### 6. Reverse LinkedList #######")
    ll.reverse()
    ll.traverse()
    
    print("\n####### 7. Sum of every two consecutive nodes #######")
    ll.pair_sum()
    
    print("\n####### End of program #######")

main()

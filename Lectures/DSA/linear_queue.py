class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinearQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_node):
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        return

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return
        
        data = self.front.data
        self.front = self.front.next
        return data

    def print(self):
        temp = self.front
        print(end="front -> ")
        while temp is not None:
            print(temp.data, end="-> ")
            temp = temp.next
        return


def main():
    queue = LinearQueue()
    while True:
        print("1. enqueue\n2. dequeue \n3. print queue\nAnything else to end\n\n")
        n = int(input())
        if n == 1:
            data = int(input("Enter data: "))
            new_node = Node(data)
            queue.enqueue(new_node)
        elif n == 2:
            print("Dequed element: ", queue.dequeue())
        elif n == 3:
            print(queue.print())
        else:
            return

main()
from stack import Stack # importing Stack written in previous question

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LQ:
    def __init__(self):
        self.start = None
        self.end = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def dequeue(self):
        if self.start is None:
            print("empty queue")
            return None

        if self.start == self.end:
            data = self.start.data
            self.start = self.end = None
            return data 

        curr = self.start
        self.start = self.start.next
        data = curr.data
        del curr
        return data

    def display(self):
        if self.start is None:
            return

        temp = self.start
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def isEmpty(self):
        return self.start is None


def reverseQueue(q : LQ):
    st = Stack()
    
    while not q.isEmpty():
        st.push(q.dequeue())

    while not st.isEmpty():
        q.enqueue(st.pop())

def mergeQueue(q1: LQ, q2: LQ) -> LQ:
    q = LQ()
    for src in (q1, q2):
        temp = src.start
        while temp:
            q.enqueue(temp.data)
            temp = temp.next
    return q

def identical(q1: LQ, q2: LQ):
    p1 = q1.start 
    p2 = q2.start

    while p1 and p2:
        if p1.data == p2.data:
            p1 = p1.next
            p2 = p2.next
        else:
            return False

    if p1 or p2:
        return False

    return True


q = LQ()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()

print("Queue: ")
q.display()

print("Reversed Queue: ")
reverseQueue(q)
q.display()
print()

print("Merge two queues")
q1 = LQ()
q2 = LQ()

q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q2.enqueue(2)
q2.enqueue(3)
q2.enqueue(4)
print("Q1")
q1.display()
print("Q2")
q2.display()
print("Merged Queue")
mergeQueue(q1, q2).display()
print()

print("Identical queues: ")
q3 = LQ()
q4 = LQ()
q3.enqueue(1)
q3.enqueue(2)
q3.enqueue(3)
q3.enqueue(4)
q4.enqueue(2)
q4.enqueue(3)
q4.enqueue(4)
print("Q1")
q3.display()
print("Q2")
q4.display()
print(end="Identical: ")
print(identical(q3, q4))

q3.dequeue()
print("Q1")
q3.display()
print("Q2")
q4.display()
print(end="Identical: ")
print(identical(q3, q4))
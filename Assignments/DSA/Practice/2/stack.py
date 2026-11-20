class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("empty stack")
            return

        temp = self.top
        data = self.top.data
        self.top = self.top.next
        del temp
        return data
    
    def peek(self):
        if self.top is None:
            print("empty stack")
            return None

        return self.top.data

    def display(self):
        temp = self.top

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def isEmpty(self):
        return self.top is None

def reverseString(s):
    st = Stack()
    for i in s:
        st.push(i)

    res = ""
    while not st.isEmpty():
        res += st.pop()

    return res

def reverseStack(stack: Stack):
    reverseStack = Stack()
    while not stack.isEmpty():
        reverseStack.push(stack.pop())

    return reverseStack

def main():
    s = "pranav abc"
    print(f"String: {s}")
    print(f"Reversed String: {reverseString(s)}")

    st1 = Stack()
    st1.push(1)
    st1.push(2)
    st1.push(3)
    st1.push(4)
    st1.push(5)
    print("Stack : ", end="")
    st1.display()
    print()
    print("Reversed Stack: ", end="")
    reverseStack(st1).display()

if __name__ == "__main__":
    main()
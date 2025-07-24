class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None 
        self.count = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_Empty():
            return "Stack is empty"
        popped_data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped_data

    def peek(self):
        if self.is_Empty():
            return "Stack is empty"
        return self.top.data

    def size(self):
        return self.count

    def is_Empty(self):
        return self.top is None

    def display(self):
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next
        return items

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Stack : ", s.display())
print("Size of stack : ", s.size())
print("Peek value : ", s.peek())
print("Popped value : ", s.pop())
print("New Stack after popping: ", s.display())
print("Size of stack after popping: ", s.size())
print("Stack is empty :", s.is_Empty())

class Stack:
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_Empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_Empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


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

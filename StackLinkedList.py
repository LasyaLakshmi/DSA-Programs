# Node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Stack LinkedList class
class Stack_LinkedList:
    def __init__(self):
        self.top = None

    # push operation
    def Push(self,data):
        NewNode = Node(data)
        NewNode.next = self.top
        self.top = NewNode

    # Pop operation
    def Pop(self):
        if self.top == None:
            print("Underflow")
            return
        else:
            popped = self.top.data
            print("popped: ",popped)
            self.top = self.top.next

    # peek operation
    def Peek(self):
        if self.top == None:
            print("Stack is empty")
            return
        else:
            peek = self.top.data
            print("Peeked: ",peek)

    # Is_Empty operation
    def is_empty(self):
       if self.top == None:
           print("is_Empty: True")
       else:
           print("is_Empty: False")

stack = Stack_LinkedList()
stack.Push(10)
stack.Push(20)
stack.Push(30)
stack.Pop()
stack.Peek()
stack.is_empty()
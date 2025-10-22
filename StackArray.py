# stack class
class stack:
    def __init__(self,max_size):
        self.stack = []
        self.max_size = max_size
    
    def push(self,data):
        if self.stack == self.max_size:
            print("Overflow")
        else:
            self.stack.append(data)
            
    def pop(self):
        if self.stack == None:
            print("underflow")
        else:
            self.stack.pop()
    
    def peek(self):
        print(self.stack[-1])

    def is_empty(self):
        if self.stack == None:
            print("Is stack Empty: Yes")
        else: 
            print("Is stack Empty: No")

# input
s = stack(5)
s.push(2)
s.push(5)
s.push(10)
print("Top element before popping: ")
s.peek()
s.pop()
print("Top element after popping: ")
s.peek()
s.is_empty()
class Node :
    def __init__(self,new_data):
       self.data = new_data
       self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None          #it will return when the linked list is empty
    
    #pushing the data

    def push (self,new_data):
        new_node = Node(new_data)
        if not new_node:
            print("\nstack is overload")
            return 
        new_node.next = self.head
        self.head = new_node

    # poping the data
        
    def pop(self):
        if self.is_empty():
            print("\nstack is underflow")
        else:
            temp = self.head
            self.head = self.head.next
            del temp

    # printing the peek of the data
            
    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            print("\nstack is empty")
            return float('-inf')
    def print_list():
        curr = st.peek()
        while curr is not None:
            print(f"{curr.head}",end = " ")
            curr=curr.next
            print()
#create a stack
st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print("peek of the stack",st.peek())
print("printing the elements from the top:")
st.pop()
st.pop()
print("top of the element after deleting :",st.peek())
# print("stack:",st.print_list())


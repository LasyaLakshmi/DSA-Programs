# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at front
    def insert_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            return

        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next

        new_node.next = self.head
        ptr.next = new_node
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = new_node  
            return

        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
        ptr.next = new_node
        new_node.next = self.head

    # Delete at front
    def delete_front(self):
        if self.head == None:
            print("List is empty!")
            return
        if self.head.next == self.head:
            print(f"{self.head.data} deleted from the front.")
            self.head = None
            return
        ptr = self.head
        while ptr.next != self.head:  
            ptr = ptr.next

        print(f"{self.head.data} deleted from the front.")
        ptr.next = self.head.next  
        self.head = self.head.next   

    # Delete at end
    def delete_end(self):
        if self.head == None:
            print("List is empty!")
            return
        if self.head.next == self.head:
            print(f"{self.head.data} deleted from the end.")
            self.head = None
            return
        ptr = self.head
        curr = self.head.next
        while curr.next != self.head:  
            ptr = curr
            curr = curr.next
        print(f"{curr.data} deleted from the end.")
        ptr.next = self.head  

    # Traverse
    def Traverse(self):
        if self.head == None:
            print("List is empty!")
            return
        ptr = self.head
        print("Circular Linked List:", end=" ")
        while ptr:
            print(ptr.data, end="-->")
            ptr = ptr.next
            if ptr == self.head:
                break
        print("NULL")

# input
cll = CircularLinkedList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.insert_front(5)

cll.Traverse()

cll.delete_front()
cll.delete_end()
cll.Traverse()

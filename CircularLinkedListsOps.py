# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node  # Circular link
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    # Insert at the beginning
    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Delete a node by value
    def delete_node(self, key):
        if self.head is None:
            print("List is empty!")
            return

        current = self.head
        prev = None

        # Case 1: Only one node
        if current.next == self.head and current.data == key:
            self.head = None
            return

        # Case 2: Deleting head node
        if current.data == key:
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        # Case 3: Deleting other nodes
        prev = self.head
        current = self.head.next
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print("Node not found!")

    # Display the Circular Linked List
    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

# Example usage
if __name__ == "__main__":
    cll = CircularLinkedList()

    cll.insert_end(10)
    cll.insert_end(20)
    cll.insert_end(30)
    cll.insert_front(5)

    cll.display()

    cll.delete_node(20)
    cll.display()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        self.append(data)

    def delete_front(self):
        if self.head:
            self.head = self.head.next
        else:
            print("List is already empty.")

    def delete_back(self):
        if not self.head:
            print("List is already empty.")
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(30)
linked_list.append(35)
linked_list.append(25)
linked_list.append(15)
print("\nInitial Linked List")
linked_list.display()

linked_list.insert_front(20)
linked_list.insert_front(40)
print("\nLinked List after front insertion")
linked_list.display()

linked_list.insert_back(50)
linked_list.insert_back(60)
print("\nLinked List after back insertion")
linked_list.display()

linked_list.delete_front()
linked_list.delete_back()
print("\nLinked List after front and back deletion")
linked_list.display()

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
            print("Deleted:", self.queue[self.front])
            self.front = self.rear = -1
        else:
            print("Deleted:", self.queue[self.front])
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            i = self.front
            print("Circular Queue:", end=" ")
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()


cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
cq.dequeue()
cq.display()

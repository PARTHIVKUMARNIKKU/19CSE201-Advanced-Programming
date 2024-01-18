class QUEUE:
    def __init__(self, size):
        self.elements = []
        self.size = size

    def empty(self):
        return len(self.elements) == 0

    def full(self):
        return len(self.elements) == self.size

    def enqueue(self, value):
        if not self.full():
            self.elements.append(value)
        else:
            print("Queue Full Exception")

    def dequeue(self):
        if not self.empty():
            print(self.elements[0])
            self.elements.pop(0)
        else:
            print("Queue Empty")

    def front(self):
        if not self.empty():
            return self.elements[0]
        else:
            return "Queue is Empty"

    def rear(self):
        if not self.empty():
            return self.elements[-1]
        else:
            return "Queue is Empty"

    def get_size(self):
        return len(self.elements)


# Example usage:
queue = QUEUE(6)
queue.enqueue(5)
queue.enqueue(23)
queue.enqueue(99)

print("Size: ", queue.get_size())
print("Front: ", queue.front())
print("Rear: ", queue.rear())

queue.enqueue(44)
queue.enqueue(24)
queue.enqueue(18)
print("Front: ", queue.front())
print("Rear: ", queue.rear())

queue.enqueue(100)

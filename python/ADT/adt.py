class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        print("Item Pushed into Stack: ", item)
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print("Popped item:", popped_item)
            return popped_item
        else:
            print("Stack is empty.")

    def top(self):
        if not self.is_empty():
            print("Top item:", self.items[-1])
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        print("Item Enqueued into Queue: ", item)
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.items.pop(0)
            print("Dequeued item:", dequeued_item)
            return dequeued_item
        else:
            print("Queue is empty.")

    def front(self):
        if not self.is_empty():
            print("Front item:", self.items[0])
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.items) == 0


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


def stack_operations():
    stack = Stack()
    no_of_push = int(input())
    for _ in range(no_of_push):
        item = input()
        stack.push(item)

    no_of_pop = int(input())
    for _ in range(no_of_pop):
        stack.pop()

    stack.top()


def queue_operations():
    queue = Queue()
    no_of_enqueue = int(input())
    for _ in range(no_of_enqueue):
        item = input()
        queue.enqueue(item)

    no_of_dequeue = int(input())
    for _ in range(no_of_dequeue):
        queue.dequeue()

    queue.front()


def doubly_linked_list_operations():
    dll = DoublyLinkedList()
    no_of_append = int(input())
    for _ in range(no_of_append):
        item = float(input())
        dll.append(item)

    print("Doubly Linked List:")
    dll.display()


def main():
    while True:
        print("Main Menu:")
        print("1 for Stack Operations")
        print("2 for Queue Operations")
        print("3 for Doubly Linked List Operations")
        print("4 to Exit the program")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            stack_operations()
        elif choice == 2:
            queue_operations()
        elif choice == 3:
            doubly_linked_list_operations()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()

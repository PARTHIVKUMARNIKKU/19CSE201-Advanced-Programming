class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_first(self, value):
        to_add = Node(value)
        to_add.next = self.head
        self.head = to_add

    def insert_last(self, value):
        to_add = Node(value)
        if self.is_empty():
            self.head = to_add
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = to_add

    def insert_after_value(self, value, already_present_value):
        to_add = Node(value)
        current = self.head
        while current:
            if current.value == already_present_value:
                to_add.next = current.next
                current.next = to_add
                return
            current = current.next
        print(f"Node with the value {already_present_value} is not found")

    def insert_after_nth(self, N):
        current = self.head
        for i in range(N - 1):
            if current:
                current = current.next
            else:
                print(f"the value {N} exceeds the limit")

    def delete_first(self):
        if self.is_empty():
            print("The list is already empty")
        else:
            self.head = self.head.next

    def delete_at_value(self, value):
        current = self.head
        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        print(f"Node with the value {value} not found")

    def delete_at_N(self, N):
        current = self.head
        for i in range(N - 1):
            if current:
                current = current.next
            else:
                print(f"{N} is out of range")
                return
        if current and current.next:
            current.next = current.next.next
        else:
            print(f"{N} is out of range")

    def display(self):
        """Displays the elements of the linked list."""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# Example usage:
linked_list = SinglyLinkedList()
linked_list.insert_last(5)
linked_list.insert_last(10)
linked_list.insert_last(15)
linked_list.insert_last(20)
linked_list.display()

linked_list.insert_first(2)
linked_list.insert_after_value(12, 10)
linked_list.insert_after_value(25, 3)
linked_list.display()-

linked_list.delete_first()
linked_list.display()

linked_list.delete_at_value(15)
linked_list.display()

linked_list.delete_at_value(5)
linked_list.delete_at_N(3)
linked_list.display()

linked_list.delete_at_N(1)
linked_list.display()

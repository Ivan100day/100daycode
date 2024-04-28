"""Defines a Node class and a Doubly linked list."""


class Node:
    """This represents a Node in a Doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def set_next(self, data):
        self.next = data

    def set_prev(self, data):
        self.prev = data

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class DoublyLinkedList:
    """This represents a Doubly linked list."""
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.root:
            first_node = self.root
            first_node.set_prev(new_node)
            self.root = new_node
            self.root.set_next(first_node)
        else:
            self.root = new_node

        self.size += 1

    def insert_at_index(self, data, index):
        new_node = Node(data)
        position = 0
        if position == index:
            self.insert_at_begin(data)
            return

        current_node = self.root
        prev_node = current_node
        while current_node is not None and position != index:
            position += 1
            prev_node = current_node
            current_node = current_node.next
        if current_node is not None:
            current_node.set_prev(new_node)
            prev_node.set_next(new_node)
            new_node.next = current_node
            new_node.prev = prev_node
            self.size += 1
        else:
            raise IndexError("Index is not present")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while current_node.next:
            current_node = current_node.next

        current_node.set_next(new_node)
        new_node.prev = current_node
        self.size += 1

    def update_node(self, val, index):
        current_node = self.root
        position = 0
        while current_node and position != index:
            position += 1
            current_node = current_node.next

        if current_node:
            current_node.set_data(val)
        else:
            raise IndexError("Index is not present")

    def remove_first_node(self):
        if self.root is None:
            return

        self.root = self.root.next
        self.root.set_prev(None)
        self.size -= 1

    def remove_at_index(self, index):
        if self.root is None:
            return

        current_node = self.root
        position = 0
        if position == index:
            self.remove_first_node()
            self.size -= 1
            return

        while current_node and position + 1 != index:
            position = position + 1
            current_node = current_node.next

        if current_node:
            if current_node.next is None:
                raise IndexError("Index is not present")

            current_node.set_next(current_node.next.next)
            current_node.next.set_prev(current_node)
            self.size -= 1
        else:
            raise IndexError("Index is not present")

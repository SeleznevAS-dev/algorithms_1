class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        node_prev = self.head

        while node is not None:
            if node.value == val and node == self.head and node == self.tail:
                self.head = None
                self.tail = None
                break

            elif node.value == val and node != self.tail and node != self.head:
                node_prev.next = node.next
                node = node_prev
                if all is False:
                    break

            elif node.value == val and node == self.head:
                self.head = node.next
                node = node.next

            elif node.value == val and node == self.tail:
                node_prev.next = None
                self.tail = node_prev
                break

            node_prev = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        result = 0
        node = self.head
        while node is not None:
            result += 1
            node = node.next
        return result

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
        else:
            prev_next = afterNode.next
            newNode.next = prev_next
            afterNode.next = newNode
            if prev_next is None:
                self.tail = newNode


class Queue:
    def __init__(self):
        self.queue = LinkedList()
        self.queue_size = 0

    # Complexity: time: O(1), space: O(1)
    def enqueue(self, item):
        node = Node(item)
        self.queue.add_in_tail(node)
        self.queue_size += 1

    # Complexity: time: O(1), space: O(1)
    def dequeue(self):
        if self.queue.head is not None:
            node = self.queue.head
            self.queue.head = node.next
            self.queue_size -= 1
            return node.value
        return None

    def size(self):
        return self.queue_size

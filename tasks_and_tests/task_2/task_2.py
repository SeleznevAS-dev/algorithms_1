class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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

        while node is not None:
            if node.value == val and node == self.head and node == self.tail:
                self.head = None
                self.tail = None
                break

            elif node.value == val and node != self.tail and node != self.head:
                node.prev.next = node.next
                node.next.prev = node.prev
                node = node.prev
                if all is False:
                    break

            elif node.value == val and node == self.head:
                self.head = node.next
                node.next.prev = None
                if all is False:
                    break

            elif node.value == val and node == self.tail:
                node.prev.next = None
                self.tail = node.prev
                break

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
        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode
        elif afterNode is None and self.head is not None:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            if afterNode.next is None:
                self.tail = newNode
            else:
                afterNode.next.prev = newNode

            newNode.next = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

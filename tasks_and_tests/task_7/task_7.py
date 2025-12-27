class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def add(self, value):
        if self.len() == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            return None

        node = self.head
        while node is not None:
            if (self.__ascending and self.compare(node.value, value) >= 0) or (
                not self.__ascending and self.compare(node.value, value) <= 0
            ):
                new_node = Node(value)
                if node.prev is not None:
                    node.prev.next = new_node
                    new_node.prev = node.prev
                else:
                    self.head = new_node

                node.prev = new_node
                new_node.next = node

                return None
            node = node.next

        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

    # No, complexity still O(n) because of worst case when we need to check all list.
    def find(self, val):
        if self.head is None:
            return None
        node = self.head
        while node is not None:
            if self.compare(node.value, val) == 0:
                return node
            elif (self.__ascending and self.compare(node.value, val) > 0) or (
                not self.__ascending and self.compare(node.value, val) < 0
            ):
                break
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            if self.compare(node.value, val) == 0:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next

                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                return None
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        return len(self.get_all())

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        clear_v1 = v1.rstrip().lstrip()
        clear_v2 = v2.rstrip().lstrip()

        if clear_v1 < clear_v2:
            return -1
        elif clear_v1 > clear_v2:
            return 1
        return 0

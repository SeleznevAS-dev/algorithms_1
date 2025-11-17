import copy
from .task_2 import LinkedList2, Node


# Course task number: 2
# Lesson task number: 2.10
# Short name: reverse_list
# Complexity: time: O(n), space: O(n)
def reverse_nodes_recursive(source_list, node):
    if node.next is None:
        next_node = node.next
        node.next, node.prev = node.prev, node.next
        return source_list
    elif node.prev is None:
        source_list.head, source_list.tail = source_list.tail, source_list.head
    next_node = node.next
    node.next, node.prev = node.prev, node.next
    return reverse_nodes_recursive(source_list, next_node)


def reverse_list(source_list):
    return reverse_nodes_recursive(source_list, source_list.head)


def test_reverse_list():
    s_list = LinkedList2()

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    s_list.add_in_tail(n1)
    s_list.add_in_tail(n2)
    s_list.add_in_tail(n3)
    s_list.add_in_tail(n4)

    s_list = reverse_list(s_list)
    assert s_list.head.value == 4
    assert s_list.head.next.value == 3

    assert s_list.tail.value == 1
    assert s_list.tail.prev.value == 2


# Course task number: 2
# Lesson task number: 2.11
# Short name: check_if_cycles
# Complexity: time: O(n), space: O(n)
def check_if_cycles(source_list):
    nodes = {}
    node = source_list.tail
    while node is not None:
        if nodes.get(node) is None:
            nodes[node] = node.value
        else:
            return True
        node = node.next

    return False


def test_check_if_cycles():
    s_list = LinkedList2()

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    s_list.add_in_tail(n1)
    s_list.add_in_tail(n2)
    s_list.add_in_tail(n3)
    s_list.add_in_tail(n4)

    assert check_if_cycles(s_list) is False

    s_list.add_in_tail(n1)

    assert check_if_cycles(s_list) is True


# Course task number: 2
# Lesson task number: 2.12
# Short name: sort_list
# Complexity: time: O(n^2), space: O(n)
def move_value_backwards_recursive(node):
    if node.prev is None or node.value >= node.prev.value:
        return
    node.value, node.prev.value = node.prev.value, node.value
    return move_value_backwards_recursive(node.prev)


def sort_list(source_list):
    node = source_list.head.next
    while node is not None:
        move_value_backwards_recursive(node)
        node = node.next
    return source_list


def test_sort_list():
    s_list = LinkedList2()

    s_list.add_in_tail(Node(4))
    s_list.add_in_tail(Node(3))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(1))

    s_list = sort_list(s_list)
    assert s_list.head.value == 1
    assert s_list.tail.value == 4


# Course task number: 2
# Lesson task number: 2.13
# Short name: merge_and_sort_two_lists
# Complexity: time: O(n^2), space: O(n)
def merge_and_sort_two_lists(list1, list2):
    list_1_to_merge = copy.deepcopy(list1)
    list_2_to_merge = copy.deepcopy(list2)
    list_1_to_merge = sort_list(list_1_to_merge)
    list_2_to_merge = sort_list(list_2_to_merge)
    len1 = list_1_to_merge.len()
    len2 = list_2_to_merge.len()
    if len2 > len1:
        list_1_to_merge, list_2_to_merge = list_2_to_merge, list_1_to_merge

    result = LinkedList2()

    for _ in range(len1 + len2):
        if list_1_to_merge.len() == 0:
            min_lst = list_2_to_merge
        elif list_2_to_merge.len() == 0:
            min_lst = list_1_to_merge
        elif list_1_to_merge.head.value < list_2_to_merge.head.value:
            min_lst = list_1_to_merge
        else:
            min_lst = list_2_to_merge

        new_node = Node(min_lst.head.value)
        result.add_in_tail(new_node)
        min_lst.delete(min_lst.head.value)

    return result


def test_merge_and_sort_two_lists():
    s_list1 = LinkedList2()

    s_list1.add_in_tail(Node(8))
    s_list1.add_in_tail(Node(6))
    s_list1.add_in_tail(Node(4))
    s_list1.add_in_tail(Node(2))

    s_list2 = LinkedList2()

    s_list2.add_in_tail(Node(3))
    s_list2.add_in_tail(Node(5))
    s_list2.add_in_tail(Node(9))

    result_list = merge_and_sort_two_lists(s_list1, s_list2)

    assert result_list.head.value == 2
    assert result_list.tail.value == 9

    assert s_list1.head.value == 8


# Course task number: 2
# Lesson task number: 2.14
# Short name: DummyNode and DummyLinkedList2
class DummyNode(Node):
    def __init__(self, v):
        super().__init__(v)
        self.dummy = True


class DummyLinkedList2(LinkedList2):
    def __init__(self):
        self.head = DummyNode(None)
        self.tail = DummyNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        self.tail.prev.next = item
        self.tail.prev = item


def test_dummy_linked_list():
    s_list = DummyLinkedList2()
    n1 = Node(1)
    n2 = Node(2)
    s_list.add_in_tail(n1)
    s_list.add_in_tail(n2)
    assert s_list.head.next.value == 1
    assert s_list.tail.prev.value == 2

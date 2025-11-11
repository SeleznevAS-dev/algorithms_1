from .task_1 import LinkedList, Node


def test_delete():
    s_list = LinkedList()

    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(3))
    s_list.add_in_tail(Node(4))

    s_list.delete(10)

    assert s_list.head.value == 1
    assert s_list.tail.value == 4
    assert s_list.len() == 4

    s_list.delete(2)

    assert s_list.head.value == 1
    assert s_list.tail.value == 4
    assert s_list.len() == 3

    s_list.delete(1)

    assert s_list.head.value == 3
    assert s_list.tail.value == 4
    assert s_list.len() == 2

    s_list.delete(4)
    assert s_list.head.value == 3
    assert s_list.tail.value == 3
    assert s_list.len() == 1

    s_list.delete(3)
    assert s_list.head is None
    assert s_list.tail is None
    assert s_list.len() == 0

    s_list.delete(1)
    assert s_list.head is None
    assert s_list.tail is None
    assert s_list.len() == 0


def test_clean():
    s_list = LinkedList()

    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(3))
    s_list.clean()
    assert s_list.head is None
    assert s_list.tail is None
    assert s_list.len() == 0

    s_list.clean()
    assert s_list.head is None
    assert s_list.tail is None
    assert s_list.len() == 0


def test_find_all():
    s_list = LinkedList()
    lst = s_list.find_all(1)
    assert lst == []

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(1)
    n4 = Node(2)
    n5 = Node(5)

    s_list.add_in_tail(n1)
    s_list.add_in_tail(n2)
    s_list.add_in_tail(n3)
    s_list.add_in_tail(n4)
    s_list.add_in_tail(n5)
    lst = s_list.find_all(1)
    assert lst == [n1, n3]

    lst = s_list.find_all(5)
    assert lst == [n5]

    lst = s_list.find_all(6)
    assert lst == []


def test_len():
    s_list = LinkedList()
    assert s_list.len() == 0

    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    assert s_list.len() == 2


def test_insert():
    s_list = LinkedList()
    n1 = Node(1)
    s_list.insert(None, n1)
    assert s_list.len() == 1
    assert s_list.head == n1
    assert s_list.tail == n1

    n2 = Node(2)
    n3 = Node(1)
    n4 = Node(2)
    s_list.add_in_tail(n2)
    s_list.add_in_tail(n3)
    s_list.add_in_tail(n4)
    
    n5 = Node(5)
    s_list.insert(n1, n5)
    assert s_list.find(5) == n5
    assert s_list.find(5).next == n2

    n6 = Node(6)
    s_list.insert(n4, n6)
    assert s_list.len() == 6
    assert s_list.tail == n6
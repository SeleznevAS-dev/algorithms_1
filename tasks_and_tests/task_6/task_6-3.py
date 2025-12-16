from .task_6 import Deque


def test_size():
    deque = Deque()
    assert deque.size() == 0
    deque.addTail(1)
    assert deque.size() == 1


def test_addTail():
    deque = Deque()
    deque.addTail(1)
    deque.addTail(2)
    assert deque.size() == 2
    assert deque.removeTail() == 2
    assert deque.removeTail() == 1


def test_addFront():
    deque = Deque()
    deque.addFront(1)
    deque.addFront(2)
    assert deque.size() == 2
    assert deque.removeFront() == 2
    assert deque.removeFront() == 1


def test_removeFront():
    deque = Deque()
    assert deque.removeFront() is None

    deque.addFront(1)
    assert deque.removeFront() == 1

    deque.addFront(2)
    deque.addFront(3)
    assert deque.size() == 2

    assert deque.removeTail() == 2
    assert deque.removeTail() == 3
    assert deque.size() == 0
    deque.addTail(1)
    assert deque.removeTail() == 1


def test_removeTail():
    deque = Deque()
    assert deque.removeTail() is None
    deque.addTail(1)
    deque.addTail(2)
    assert deque.size() == 2
    assert deque.removeTail() == 2
    assert deque.removeTail() == 1

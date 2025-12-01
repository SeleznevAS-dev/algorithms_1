from .task_4 import Stack


def test_size():
    stack = Stack()

    assert stack.size() == 0
    stack.push(1)
    assert stack.size() == 1
    stack.push("2")
    assert stack.size() == 2
    stack.push(3.14)
    assert stack.size() == 3


def test_push():
    stack = Stack()

    stack.push(1)
    assert stack.peek() == 1
    assert stack.size() == 1
    stack.push(2)
    assert stack.peek() == 2


def test_pop():
    stack = Stack()

    stack.push(1)
    stack.push("2")
    stack.push(3.14)
    assert stack.pop() == 3.14
    assert stack.pop() == "2"
    assert stack.pop() == 1


def test_peek():
    stack = Stack()

    stack.push(1)
    assert stack.peek() == 1
    stack.push("2")
    assert stack.peek() == "2"
    stack.push(3.14)
    assert stack.peek() == 3.14

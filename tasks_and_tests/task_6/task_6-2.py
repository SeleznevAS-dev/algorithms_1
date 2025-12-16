from .task_6 import Deque
from tasks_and_tests.task_3.task_3 import DynArray
from tasks_and_tests.task_4.task_4 import Stack


# Course task number: 6
# Lesson task number: 6.3
# Short name: check_if_palindrome
# Complexity: time: O(n), space: O(n)
def check_if_palindrome(string):
    deque = Deque()
    for i in string:
        deque.addTail(i)

    while deque.size() > 1:
        front = deque.removeFront()
        back = deque.removeTail()
        if front != back:
            return False
    return True


# Course task number: 6
# Lesson task number: 6.4
# Short name: MinDeque
class MinDeque(Deque):
    def __init__(self):
        super().__init__()
        self.min_elements = []

    def addFront(self, item):
        super().addFront(item)
        for i in range(len(self.min_elements)):
            if self.min_elements[i] >= item:
                self.min_elements.insert(i, item)
                return
        self.min_elements.append(item)

    def addTail(self, item):
        super().addTail(item)
        for i in range(len(self.min_elements)):
            if self.min_elements[i] >= item:
                self.min_elements.insert(i, item)
                return
        self.min_elements.append(item)

    def removeFront(self):
        item = super().removeFront()
        if item is not None:
            self.min_elements.remove(item)

    def removeTail(self):
        item = super().removeTail()
        if item is not None:
            self.min_elements.remove(item)

    def getMin(self):
        if not self.min_elements:
            return None
        return self.min_elements[0]


def test_MinDeque():
    min_deque = MinDeque()
    min_deque.addTail(3)
    min_deque.addTail(4)
    min_deque.addTail(1)
    min_deque.addTail(2)

    assert min_deque.getMin() == 1

    min_deque.removeTail()
    min_deque.removeTail()
    assert min_deque.getMin() == 3


# Course task number: 6
# Lesson task number: 6.5
# Short name: DynArrayDeque
class ModifiedDynArray(DynArray):
    def __init__(self):
        super().__init__()
        self.head_index = self.capacity // 2

    def expand(self):
        new_capacity = self.capacity * 2
        new_array = super().make_array(new_capacity)
        new_head = (new_capacity - self.count) // 2
        for i in range(self.count):
            new_array[new_head + i] = self.array[self.head_index + i]
        self.array = new_array
        self.capacity = new_capacity
        self.head_index = new_head

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[self.head_index + i]

    def append(self, itm):
        if self.count == self.capacity or self.head_index + self.count == self.capacity:
            self.expand()
        self.array[self.head_index + self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError("Index is out of bounds")

        if i == self.count:
            self.append(itm)
            return

        if i == 0:
            if self.count == self.capacity or self.head_index == 0:
                self.expand()
            self.head_index -= 1
            self.array[self.head_index] = itm
            self.count += 1
            return

        raise IndexError("Index is out of bounds")

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")

        if i == 0:
            self.head_index += 1
            self.count -= 1
            if self.count == 0:
                self.head_index = self.capacity // 2
        elif i == self.count - 1:
            self.count -= 1
        else:
            raise IndexError("Index is out of bounds")


class DynArrayDeque(Deque):
    def __init__(self):
        super().__init__()
        self.deque = ModifiedDynArray()

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        item = self.deque[0]
        self.deque.delete(0)
        return item

    def removeTail(self):
        if self.size() == 0:
            return None
        last_index = self.deque.count - 1
        item = self.deque[last_index]
        self.deque.delete(last_index)
        return item

    def size(self):
        return self.deque.count


def test_DynArrayDeque():
    dyn_array_deque = DynArrayDeque()
    dyn_array_deque.addTail(1)
    dyn_array_deque.addTail(2)
    dyn_array_deque.addFront(0)

    assert dyn_array_deque.size() == 3
    assert dyn_array_deque.removeFront() == 0
    assert dyn_array_deque.removeTail() == 2
    assert dyn_array_deque.size() == 1


# Course task number: 6
# Lesson task number: 6.6
# Short name: is_parens_balanced
# Complexity: time: O(n), space: O(n)
def is_parens_balanced(string):
    stack = Stack()
    deque = Deque()
    for s in string:
        deque.addTail(s)

    pairs = {"(": ")", "[": "]", "{": "}"}

    while deque.size() > 0:
        s = deque.removeFront()
        if pairs.get(s) is not None:
            stack.push(s)
            continue

        if stack.size() == 0:
            return False
        top = stack.pop()
        if pairs[top] != s:
            return False

    return stack.size() == 0


def test_is_parens_balanced():
    assert is_parens_balanced("[(())]") is True
    assert is_parens_balanced("{((){((([])))}())}") is True
    assert is_parens_balanced("") is True
    assert is_parens_balanced("{(())") is False
    assert is_parens_balanced("[{}()") is False


# Рефлексия
# 5. Баланс открывающих и закрывающих скобок трёх типов.
# Реализовал неправильно, использовал три стека под каждый тип скобок.

# 6. Текущий минимальный элемент в стеке за O(1).
# Реализовал полностью правильно.

# 7. Среднее значение всех элементов в стеке за O(1).
# Реализовал полностью правильно.

# 8. Постфиксная запись выражения.
# Реализовал с ошибкой: копипастил вычисление аргументов для каждой операции.

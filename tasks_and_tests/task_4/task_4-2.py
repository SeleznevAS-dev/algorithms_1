from .task_4 import Stack


# Course task number: 4
# Lesson task number: 4.5
# Short name: is_parens_balanced
# Complexity: time: O(n), space: O(n)
def is_parens_balanced(string: str) -> bool:
    stack = Stack()

    for i in string:
        if i == "(":
            stack.push(i)
        elif i == ")" and stack.size() > 0:
            stack.pop()
    if stack.size() == 0:
        return True

    return False


def test_is_parens_balanced():
    assert is_parens_balanced("(())") is True
    assert is_parens_balanced("(()((())()))") is True
    assert is_parens_balanced("(()") is False
    assert is_parens_balanced("))((") is False


# Course task number: 4
# Lesson task number: 4.6
# Short name: is_parens_balanced_modified
# Complexity: time: O(n), space: O(n)
def is_parens_balanced_modified(string: str) -> bool:
    stack1 = Stack()  # for "()"
    stack2 = Stack()  # for "{}"
    stack3 = Stack()  # for "[]"

    for i in string:
        if i == "(" or i == ")":
            stack = stack1
        elif i == "{" or i == "}":
            stack = stack2
        else:
            stack = stack3

        if i == "(" or i == "{" or i == "[":
            stack.push(i)
        elif (i == ")" or i == "}" or i == "]") and stack.size() > 0:
            stack.pop()

    if stack1.size() == 0 and stack2.size() == 0 and stack3.size() == 0:
        return True

    return False


def test_is_parens_balanced_modified():
    assert is_parens_balanced_modified("[(())]") is True
    assert is_parens_balanced_modified("{((){((([]))}()))}") is True
    assert is_parens_balanced_modified("{(())") is False
    assert is_parens_balanced_modified("[{}()") is False


# Course task number: 4
# Lesson task number: 4.7
# Short name: MinStack
class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def push(self, value):
        super().push(value)
        if self.min_stack.size() == 0 or value <= self.min_stack.peek():
            self.min_stack.push(value)

    def pop(self):
        popped = super().pop()
        if popped is not None and popped == self.min_stack.peek():
            self.min_stack.pop()
        return popped

    def min(self):
        if self.min_stack.size() > 0:
            return self.min_stack.peek()
        return None


def test_MinStack():
    stack = MinStack()
    stack.push(3)
    stack.push(1)
    stack.push(2)

    assert stack.min() == 1
    stack.pop()
    stack.pop()
    assert stack.min() == 3


# Course task number: 4
# Lesson task number: 4.8
# Short name: AvgStack
class AvgStack(Stack):
    def __init__(self):
        super().__init__()
        self.sum = 0

    def push(self, value):
        super().push(value)
        self.sum += value

    def pop(self):
        popped = super().pop()
        self.sum -= popped

    def average(self):
        return self.sum / self.size()


def test_AvgStack():
    stack = AvgStack()
    n1 = 3
    n2 = 1
    n3 = 2
    stack.push(n1)
    stack.push(n2)
    stack.push(n3)
    sm = n1 + n2 + n3

    assert stack.average() == sm / 3

    n4 = 10
    sm += n4
    stack.push(n4)

    assert stack.average() == sm / 4


# Course task number: 4
# Lesson task number: 4.9
# Short name: postfix_stack
def postfix_stack(string: str) -> int:
    stack1 = Stack()
    stack2 = Stack()
    string = string[::-1]
    for i in string:
        if i != " ":
            stack1.push(i)

    while stack1.size() > 0:
        n = stack1.pop()
        if n == "+":
            n1 = stack2.pop()
            n2 = stack2.pop()

            stack2.push(n1 + n2)

        elif n == "*":
            n1 = stack2.pop()
            n2 = stack2.pop()

            stack2.push(n1 * n2)

        elif n == "=":
            return stack2.pop()

        else:
            stack2.push(int(n))

    return stack2.pop()


def test_postfix_stack():
    assert postfix_stack("1 2 + 3 * =") == 9
    assert postfix_stack("8 2 + 5 * 9 + =") == 59


# Рефлексия
# Задание 9: Решено верно.
# Задание 10: Не так понял суть задания, поэтому решил неверно. Проверил, есть ли дублирующиеся узлы в списке.
# Задание 11: Решено верно, использовал сортировку вставками.
# Задание 12: Грубая ошибка: моё решение предусматривает только два списка, остальное правильно.
# Задание 13: Ошибка: сделал Dummy через флаг, по сути не реализовав его, а просто добавив флажок.

from tasks_and_tests.task_3.task_3 import DynArray


class Stack:
    def __init__(self):
        self.stack = DynArray()

    def size(self):
        return len(self.stack)

    # Complexity: time: O(n), space: O(n)
    def pop(self):
        if self.size() > 0:
            index = self.size() - 1
            elem = self.stack[index]
            self.stack.delete(index)
            return elem
        return None

    # Complexity: time: O(1), space: O(n)
    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() > 0:
            index = self.size() - 1
            elem = self.stack[index]
            return elem
        return None


# Task 2
class StackReversed:
    def __init__(self):
        self.stack = DynArray()

    def size(self):
        return len(self.stack)

    # Complexity: time: O(n), space: O(n)
    def pop(self):
        if self.size() > 0:
            index = 0
            elem = self.stack[index]
            self.stack.delete(index)
            return elem
        return None

    # Complexity: time: O(n), space: O(n)
    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.size() > 0:
            index = 0
            elem = self.stack[index]
            return elem
        return None

# Task 3
# Cycle will work in two ways: if stack size is even, it will print two elements of stack per cycle. If it's odd, cycle will raise IndexError exception.
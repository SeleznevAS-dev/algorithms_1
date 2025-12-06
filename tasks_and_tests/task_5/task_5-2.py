import ctypes
from .task_5 import Queue
from tasks_and_tests.task_4.task_4 import Stack


# Course task number: 5
# Lesson task number: 5.3
# Short name: round_queue
# Complexity: time: O(N), space: O(N)
def round_queue(queue: Queue, N: int):
    for _ in range(N):
        num = queue.dequeue()
        queue.enqueue(num)


def test_round_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    round_queue(queue, 2)

    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2


# Course task number: 5
# Lesson task number: 5.4
# Short name: StackQueue
class StackQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, item):
        self.stack_1.push(item)

    def dequeue(self):
        if self.stack_1.size == 0:
            return None

        while self.stack_1.size() > 0:
            num = self.stack_1.pop()
            if self.stack_1.size() == 0:
                break
            self.stack_2.push(num)

        while self.stack_2.size() > 0:
            self.stack_1.push(self.stack_2.pop())

        return num

    def size(self):
        return self.stack_1.size()


def test_StackQueue():
    queue = StackQueue()
    queue.enqueue(1)
    assert queue.size() == 1
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


# Course task number: 5
# Lesson task number: 5.5
# Short name: ReverseQueue
# Complexity: time: O(N), space: O(N)
class ReverseQueue(Queue):
    def reverse(self):
        lst = []
        while self.size() > 0:
            lst.append(self.dequeue())
        lst.reverse()
        for i in lst:
            self.enqueue(i)


def test_ReverseQueue():
    queue = ReverseQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.reverse()
    assert queue.dequeue() == 3
    assert queue.dequeue() == 2
    assert queue.dequeue() == 1


# Course task number: 5
# Lesson task number: 5.6
# Short name: StaticArrQueue
class StaticArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
        self.start_index = 0

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.start_index + self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    def append(self, itm):
        if self.count + 1 > self.capacity:
            raise IndexError("Reached maximum items of array")

        if self.start_index + self.count > self.capacity:
            self.shift_arr()
        self.array[self.start_index + self.count] = itm
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.start_index + self.count:
            raise IndexError("Index is out of bounds")
        self.array[i] = ctypes.py_object
        self.count -= 1
        self.start_index += 1
        if self.count == 0:
            self.start_index = 0

    def shift_arr(self):
        new_array = self.make_array(self.capacity)
        i = 0
        for j in range(self.start_index, self.start_index + self.count):
            new_array[i] = self.array[j]
            self.count -= 1
            i += 1
        self.start_index = 0
        self.array = new_array


class StaticArrQueue:
    def __init__(self):
        self.queue = StaticArray()

    def is_queue_full(self):
        if self.queue.count == self.queue.capacity:
            return True
        return False

    def enqueue(self, item):
        if self.is_queue_full():
            raise IndexError("Reached maximum items of queue")
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            item = self.queue[self.queue.start_index]
            self.queue.delete(self.queue.start_index)
            return item
        return None

    def size(self):
        return len(self.queue)


def test_StaticArrQueue():
    queue = StaticArrQueue()
    queue.enqueue(1)
    assert queue.size() == 1
    queue.enqueue(2)
    assert queue.size() == 2
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.size() == 2
    assert queue.dequeue() == 2
    assert queue.size() == 1
    assert queue.dequeue() == 3


# Рефлексия
# 6. Динамический массив на основе банковского метода.
# Реализовал немного не так: цена учитывается только для вставки, при удалении такого нет. Цена так же равно количеству элементов. В целом не до конца понял, как это в идеале должно работать.

# 7. Многомерный динамический массив.
# Реализовал не так: вместо большого одномерного массива создал несколько одномерных, и работал с ними.

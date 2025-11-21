import ctypes
from .task_3 import DynArray


# Course task number: 3
# Lesson task number: 3.5
# Short name: BankDynArray
class BankDynArray(DynArray):
    def __init__(self):
        super().__init__()
        self.price = self.capacity
        self.cost = 3
        self.sum_cost = 0

    def resize(self, new_capacity):
        super().resize(new_capacity)

        self.price *= 2
        self.sum_cost = 0

    def append(self, itm):
        self.sum_cost += 3
        if self.sum_cost >= self.price:
            self.resize(2 * self.capacity)

        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError("Index is out of bounds")

        self.sum_cost += 3
        if self.sum_cost >= self.price:
            self.resize(2 * self.capacity)

        if i == self.count:
            self.array[i] = itm
            self.count += 1
        else:
            new_array = self.make_array(self.capacity)
            shift = 0
            for j in range(self.count + 1):
                if j == i:
                    new_array[j] = itm
                    self.count += 1
                    shift += 1
                    continue
                new_array[j] = self.array[j - shift]
            self.array = new_array


def test_BankDynArray():
    array = BankDynArray()
    array.append(1)
    assert array.sum_cost == 3
    array.append(2)
    assert array.sum_cost == 6
    array.append(3)
    array.append(4)
    array.append(5)
    array.append(6)
    assert array.sum_cost == 0
    assert array.count == 6
    assert array.capacity == 32


# Course task number: 3
# Lesson task number: 3.6
# Short name: MultiDynArray
class MultiDynArray:
    def __init__(self, num_of_dimensions, capacity):
        self.array = (num_of_dimensions * ctypes.py_object)()
        self.count = 0
        for _ in range(num_of_dimensions):
            new_array = self.make_simple_array(capacity)
            self.array[self.count] = new_array
            self.count += 1

    def make_simple_array(self, capacity):
        new_array = DynArray()
        new_array.resize(capacity)
        return new_array

    def __len__(self):
        return self.count

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]


def test_MultiDynArray():
    array = MultiDynArray(2, 8)
    array[0].append(1)
    assert array[0][0] == 1
    assert array[0].capacity == 8
    array[0].append(2)
    array[0].append(3)
    array[0].append(4)
    array[0].append(5)
    array[0].append(6)
    array[0].append(7)
    array[0].append(8)
    array[0].append(9)
    assert array[0].capacity == 16

    array[1].append(2)
    assert array[1][0] == 2


# Reflex

# Additional task 1 done almost good, but didn't throw exception if len's are not equal.

from .task_7 import OrderedList


# Course task number: 7
# Lesson task number: 7.8
# Short name: DublicateDeleteOrderedList
# Complexity: time: O(n), space: O(n)
class DublicateDeleteOrderedList(OrderedList):
    def delete_dublicates(self):
        lst = []
        node = self.head

        while node is not None:
            if node.value in lst:
                self.delete(node.value)
            else:
                lst.append(node.value)
            node = node.next


def test_dublicate_delete_ordered_list():
    odl = DublicateDeleteOrderedList(True)
    odl.add(1)
    odl.add(1)
    odl.add(1)

    odl.delete_dublicates()

    values = [node.value for node in odl.get_all()]
    assert values == [1]


# Course task number: 7
# Lesson task number: 7.9
# Short name: MergeTwoOrderedList
# Complexity: time: O(n), space: O(n)
class MergeTwoOrderedList(OrderedList):
    def merge(self, other):
        merged = MergeTwoOrderedList(self._OrderedList__ascending)

        node1 = self.head
        node2 = other.head

        while node1 is not None and node2 is not None:
            if (self._OrderedList__ascending and node1.value <= node2.value) or (
                not self._OrderedList__ascending and node1.value >= node2.value
            ):
                merged.add(node1.value)
                node1 = node1.next
            else:
                merged.add(node2.value)
                node2 = node2.next

        while node1 is not None:
            merged.add(node1.value)
            node1 = node1.next

        while node2 is not None:
            merged.add(node2.value)
            node2 = node2.next

        return merged


def test_merge_two_ordered_list():
    odl1 = MergeTwoOrderedList(True)
    odl1.add(1)
    odl1.add(3)
    odl1.add(5)

    odl2 = MergeTwoOrderedList(True)
    odl2.add(2)
    odl2.add(4)
    odl2.add(6)

    merged = odl1.merge(odl2)

    values = [node.value for node in merged.get_all()]
    assert values == [1, 2, 3, 4, 5, 6]


# Course task number: 7
# Lesson task number: 7.10
# Short name: CheckSubarrOrderedList
# Complexity: time: O(n), space: O(1)
class CheckSubarrOrderedList(OrderedList):
    def check_subarr(self, subarr):
        index = 0
        node = self.head
        while node is not None:
            if node.value == subarr[index]:
                index += 1
                if index == len(subarr):
                    return True
            else:
                index = 0
            node = node.next
        return False


def test_check_subarr_ordered_list():
    odl = CheckSubarrOrderedList(True)
    odl.add(1)
    odl.add(2)
    odl.add(3)
    odl.add(4)
    odl.add(5)

    assert odl.check_subarr([2, 3, 4]) is True
    assert odl.check_subarr([2, 3, 5]) is False


# Course task number: 7
# Lesson task number: 7.11
# Short name: MostFrequentMatchOrderedList
# Complexity: time: O(n), space: O(n)
class MostFrequentMatchOrderedList(OrderedList):
    def most_frequent_match(self):
        freq_dict = {}
        node = self.head
        while node is not None:
            if node.value in freq_dict:
                freq_dict[node.value] += 1
            else:
                freq_dict[node.value] = 1
            node = node.next

        max_count = 0
        most_frequent_value = None
        for item, value in freq_dict.items():
            if value > max_count:
                max_count = value
                most_frequent_value = item
        return most_frequent_value


def test_most_frequent_match_ordered_list():
    odl = MostFrequentMatchOrderedList(True)
    odl.add(1)
    odl.add(2)
    odl.add(2)
    odl.add(3)
    odl.add(3)
    odl.add(3)

    assert odl.most_frequent_match() == 3


# Course task number: 7
# Lesson task number: 7.12
# Short name: BinaryFindOrderedList
# Complexity: time: O(log n), space: O(1)
class BinaryFindOrderedList(OrderedList):
    def binary_find(self, val):
        left = 0
        right = self.len() - 1
        while left <= right:
            mid = (left + right) // 2
            node = self.head
            for _ in range(mid):
                node = node.next

            if self.compare(node.value, val) == 0:
                return node
            elif (
                self._OrderedList__ascending and self.compare(node.value, val) < 0
            ) or (
                not self._OrderedList__ascending and self.compare(node.value, val) > 0
            ):
                left = mid + 1
            else:
                right = mid - 1
        return None


def test_binary_find_ordered_list():
    odl = BinaryFindOrderedList(True)
    odl.add(1)
    odl.add(2)
    odl.add(3)
    odl.add(4)
    odl.add(5)

    assert odl.binary_find(3).value == 3
    assert odl.binary_find(6) is None


# Рефлексия
# 3. Вращение очереди по кругу на N элементов.
# Сделано полностью правильно.

# 4. Очередь с помощью двух стеков.
# Кладется правильно, в один стек, но забирается неправильно, перегоняя каждый раз.

# 5. Обращение всех элементов в очереди в обратном порядке.
# Сделано вообще неправильно: использовал список и просто переворачивал его через reverse.

# 6. Циклическая буферную очередь на базе статического массива фиксированного размера.
# Сделал только по сути через head, а за tail взял индекс head + количество элементов. При этом если добавляется за границы capacity, то вместо перескакивания сделал через сдвиг элементов, что ошибка.

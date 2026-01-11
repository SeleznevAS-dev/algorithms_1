from .task_9 import NativeDictionary
from ..task_7.task_7 import OrderedList


# Course task number: 9
# Lesson task number: 9.5
# Short name: OdreredListNativeDictionary
class OdreredListNativeDictionary(NativeDictionary):
    def __init__(self, sz):
        self.slots = OrderedList(True)
        self.values = []
        self.size = sz

    def find_index(self, key_hash):
        index = 0
        node = self.slots.head
        while node is not None:
            if node.value == key_hash:
                return index
            index += 1
            node = node.next
        return None

    def is_key(self, key):
        index = super().hash_fun(key)
        return self.find_index(index) is not None

    # Complexity: Time: O(n)
    def put(self, key, value):
        index = super().hash_fun(key)
        list_index = self.find_index(index)
        if list_index is not None:
            self.values[list_index] = value
        else:
            self.slots.add(index)
            list_index = self.find_index(index)
            self.values.insert(list_index, value)

    # Complexity: Time: O(n)
    def get(self, key):
        index = super().hash_fun(key)
        list_index = self.find_index(index)
        if list_index is not None:
            return self.values[list_index]
        return None

    # Complexity: Time: O(n)
    def delete(self, key):
        index = super().hash_fun(key)
        list_index = self.find_index(index)
        if list_index is not None:
            self.slots.delete(index)
            self.values.pop(list_index)


def test_OdreredListNativeDictionary():
    ond = OdreredListNativeDictionary(17)
    ond.put("abc", 1)
    assert ond.get("abc") == 1

    ond.put("abcd", 2)
    assert ond.get("abcd") == 2

    ond.put("abc", 3)
    assert ond.get("abc") == 3

    assert ond.is_key("abc") is True
    assert ond.is_key("abcd") is True
    assert ond.is_key("ab") is False

    ond.delete("abc")
    assert ond.get("abc") is None
    assert ond.is_key("abc") is False


# Course task number: 9
# Lesson task number: 9.6
# Short name: BitNativeDictionary
class BitNativeDictionary:
    def __init__(self, sz, bit_length):
        self.size = sz
        self.bit_length = bit_length
        self.values = [None] * self.size

    def _key_to_index(self, key):
        return int(key, 2)

    def is_key(self, key):
        index = self._key_to_index(key)
        return self.values[index] is not None

    def put(self, key, value):
        index = self._key_to_index(key)
        self.values[index] = value
        return index

    def get(self, key):
        index = self._key_to_index(key)
        return self.values[index]

    def delete(self, key):
        index = self._key_to_index(key)
        if self.values[index] is not None:
            self.values[index] = None
            return True
        return False


def test_BitNativeDictionary():
    bsd = BitNativeDictionary(17, 4)
    bsd.put("1010", 1)
    assert bsd.get("1010") == 1

    bsd.put("1111", 2)
    assert bsd.get("1111") == 2

    bsd.put("1010", 3)
    assert bsd.get("1010") == 3

    assert bsd.is_key("1010") is True
    assert bsd.is_key("1111") is True
    assert bsd.is_key("0000") is False

    bsd.delete("1010")
    assert bsd.get("1010") is None
    assert bsd.is_key("1010") is False


# Рефлексия
# 9. Слияние двух упорядоченных списков в один.
# В целом сделано правильно, просто слил два отсортированных списка в новый.

# 10. Проверка наличия заданного упорядоченного под-списка в текущем списке.
# В ранних курсах было похожее задание, вспомнил решение оттуда, только не учел нюанс, что имею дело с упорядоченным списком и можно сразу прерывать цикл, если элемент подсписка меньше.

# 11. Ищем наиболее часто встречающееся значение в списке.
# Сделал тупо: собрал количество повторений в словарь, можно было сделать намного лучше.

# 12. Индекс заданного элемента в списке за O(log N).
# Невнимательно прочитал условие задачи, что нужно возвращать именно индекс элемента, из-за этого просто вовзращал узел.

from .task_8 import HashTable

import hashlib


# Course task number: 8
# Lesson task number: 8.3
# Short name: DynamicHashTable
class DynamicHashTable(HashTable):
    def __init__(self, sz, stp):
        super().__init__(sz, stp)

        self.indexes = []

    def _resize_and_rehash(self):
        old_slots = []
        for i in self.indexes:
            old_slots.append(self.slots[i])

        self.size *= 2
        self.slots = [None] * self.size
        self.indexes = []

        for slot in old_slots:
            new_index = super().put(slot)
            if new_index is not None:
                self.indexes.append(new_index)

    def put(self, value):
        index = super().put(value)

        if index is not None:
            self.indexes.append(index)

        if len(self.indexes) / self.size > 0.75:
            self._resize_and_rehash()

        return index


def test_dynamic_hash_table():
    dht = DynamicHashTable(4, 1)

    for i in range(3):
        dht.put(f"{i}")

    assert dht.size == 4

    dht.put("3")
    assert dht.size == 8


# Course task number: 8
# Lesson task number: 8.4
# Short name: MultiHashTable
class MultiHashTable(HashTable):
    def hash_fun2(self, value):
        value_bytes = bytearray(value, encoding="UTF-8")
        sm = 0
        for i in range(len(value_bytes)):
            sm += (i + 1) * value_bytes[i]

        index = (sm % (self.size - 1)) + 1

        return index

    def put(self, value):
        start = self.hash_fun(value)
        if self.slots[start] is None:
            self.slots[start] = value
            return start

        step = self.hash_fun2(value)
        for i in range(1, self.size):
            index = (start + i * step) % self.size
            if self.slots[index] is None:
                self.slots[index] = value
                return index

        return None


# Вероятность коллизий в MultiHashTable уменьшилась за счёт использования второй хеш-функции, производительность осталась такой же.


def test_multi_hash_table():
    ht = MultiHashTable(11, 1)
    index = ht.hash_fun("abc")
    ht.slots[index] = "test"

    idx = ht.put("abc")
    assert idx is not None
    assert idx != index
    assert ht.slots[idx] == "abc"


# Course task number: 8
# Lesson task number: 8.5
# Short name: SaltHashTable
class SaltHashTable(HashTable):
    def __init__(self, sz, stp, salt):
        super().__init__(sz, stp)
        self.salt = salt

    def hash_fun(self, value):
        h = hashlib.sha256()
        h.update(self.salt.encode("UTF-8"))
        h.update(value.encode("UTF-8"))
        digest = h.digest()
        sm = int.from_bytes(digest[:8])
        return sm % self.size


def test_salt_hash_table():
    value = "abc"

    ht1 = SaltHashTable(17, 3, "salt")
    ht2 = SaltHashTable(17, 3, "pepper")

    i1 = ht1.hash_fun(value)
    i1_again = ht1.hash_fun(value)
    i2 = ht2.hash_fun(value)

    assert i1 == i1_again
    assert i1 != i2


# Рефлексия
# 4. Проверка строки на палиндром.
# Сделано полностью правильно.

# 5. Минимальный элемент деки за O(1).
# Сделал через одну деку, но вариант с двумя деками был бы намного лучше.

# 6. Двусторонняя очередь на базе динамического массива.
# Сделал с ошибкой: смешал в одном классе логику двух структур данных.

from .task_10 import PowerSet


# Course task number: 10
# Lesson task number: 10.4
# Short name: DecartPowerSet
# Complexity: Time: O(n*m), Space: O(n*m)
class DecartPowerSet(PowerSet):
    def decart_multiply(self, set2: PowerSet):
        ans = PowerSet()

        for i in self.set.values():
            for j in set2.set.values():
                if ans.get((i, j)) is False:
                    ans.put((i, j))
        return ans


def test_DecartPowerSet():
    ps1 = DecartPowerSet()
    ps1.put(1)
    ps1.put(2)
    ps1.put(3)

    ps2 = DecartPowerSet()
    ps2.put(1)
    ps2.put(2)
    ps2.put(3)

    assert ps1.decart_multiply(ps2).set == {
        (1, 1): (1, 1),
        (1, 2): (1, 2),
        (1, 3): (1, 3),
        (2, 1): (2, 1),
        (2, 2): (2, 2),
        (2, 3): (2, 3),
        (3, 1): (3, 1),
        (3, 2): (3, 2),
        (3, 3): (3, 3),
    }


# Course task number: 10
# Lesson task number: 10.5
# Short name: multi_intersection
# Complexity: Time: O(n*m), Space: O(n)
def multi_intersection(sets: list[PowerSet]):
    min_length = sets[0].size()
    min_set = sets[0]
    for i in sets:
        if i.size() < min_length:
            min_length = i.size()
            min_set = i

    del sets[sets.index(min_set)]
    ans = PowerSet()
    for i in min_set.set.values():
        all_have = True
        for j in sets:
            if not j.get(i):
                all_have = False
                break
        if all_have:
            ans.put(i)

    return ans


def test_multi_intersection():
    ps1 = PowerSet()
    ps1.put(1)
    ps1.put(2)
    ps1.put(3)

    ps2 = PowerSet()
    ps2.put(2)
    ps2.put(3)
    ps2.put(4)

    ps3 = PowerSet()
    ps3.put(2)
    ps3.put(5)

    result = multi_intersection([ps1, ps2, ps3])
    assert result.set == {2: 2}


# Course task number: 10
# Lesson task number: 10.6
# Short name: BagPowerSet
# Complexity: Time: O(n), Space: O(n)
class BagPowerSet:
    def __init__(self):
        self.set = []

    def put(self, value):
        self.set.append(value)

    def delete_one(self, value):
        if value in self.set:
            self.set.remove(value)
            return True
        return False

    def get_elements_with_counts(self):
        counts = {}
        for item in self.set:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        return counts


def test_BagPowerSet():
    bps = BagPowerSet()
    bps.put(1)
    bps.put(2)
    bps.put(1)
    bps.put(3)
    bps.put(2)
    bps.put(1)

    assert bps.get_elements_with_counts() == {1: 3, 2: 2, 3: 1}

    assert bps.delete_one(2) is True
    assert bps.get_elements_with_counts() == {1: 3, 2: 1, 3: 1}

    assert bps.delete_one(4) is False
    assert bps.get_elements_with_counts() == {1: 3, 2: 1, 3: 1}


# Рефлексия
# 3. Динамическая хэш-таблица.
# Сделал неправильно через наследование, нужно было через композицию.

# 5. ddos хэш-таблицы и соль.
# Тоже сделал неправильно, соль получилась статическая, не додумался хранить соль к каждому значению.

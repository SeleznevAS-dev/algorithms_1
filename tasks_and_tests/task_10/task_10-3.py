from .task_10 import PowerSet
import time


def test_put():
    ps = PowerSet()
    assert ps.size() == 0
    ps.put(1)
    assert ps.size() == 1
    ps.put(1)
    assert ps.size() == 1
    assert ps.get(1) is True


def test_remove():
    ps = PowerSet()
    ps.put(1)
    assert ps.size() == 1
    assert ps.remove(1) is True
    assert ps.size() == 0
    assert ps.get(0) is False
    assert ps.remove(1) is False


def test_intersection():
    ps1 = PowerSet()
    ps1.put(1)
    ps1.put(2)
    ps1.put(3)

    ps2 = PowerSet()
    ps2.put(2)
    ps2.put(4)

    assert ps1.intersection(ps2).size() == 1

    ps2.put(1)
    ps2.put(3)

    assert ps1.intersection(ps2).size() == 3

    ps1 = PowerSet()
    ps1.put(1)
    ps1.put(3)

    ps2 = PowerSet()
    ps2.put(2)
    ps2.put(4)

    assert ps1.intersection(ps2).size() == 0


def test_union():
    ps1 = PowerSet()
    ps1.put(1)
    ps1.put(2)
    ps1.put(3)

    ps2 = PowerSet()
    ps2.put(2)
    ps2.put(4)

    assert ps1.union(ps2).size() == 4

    ps2 = PowerSet()

    assert ps1.union(ps2).size() == 3


def test_difference():
    ps1 = PowerSet()
    ps1.put(1)
    ps1.put(2)
    ps1.put(3)

    ps2 = PowerSet()
    ps2.put(2)
    ps2.put(4)

    assert ps1.difference(ps2).size() == 2

    ps2 = PowerSet()
    ps2.put(4)
    ps2.put(5)

    assert ps1.difference(ps2).size() == 3

    ps2 = PowerSet()
    ps2.put(1)
    ps2.put(2)
    ps2.put(3)

    assert ps1.difference(ps2).size() == 0


def test_issubset():
    ps1 = PowerSet()
    ps1.put(1)
    ps1.put(2)
    ps1.put(3)

    ps2 = PowerSet()
    ps2.put(2)

    assert ps1.issubset(ps2) is True

    ps1 = PowerSet()
    ps1.put(1)
    ps1.put(2)
    ps1.put(3)

    ps2 = PowerSet()
    ps2.put(1)
    ps2.put(2)
    ps2.put(3)
    ps2.put(4)
    ps2.put(5)

    assert ps1.issubset(ps2) is False

    ps1 = PowerSet()
    ps1.put(1)
    ps1.put(2)
    ps1.put(3)

    ps2 = PowerSet()
    ps2.put(1)
    ps2.put(2)
    ps2.put(4)

    assert ps1.issubset(ps2) is False


def test_equals():
    ps1 = PowerSet()
    ps1.put(1)
    ps1.put(2)
    ps1.put(3)

    ps2 = PowerSet()
    ps2.put(1)
    ps2.put(2)
    ps2.put(3)

    assert ps1.equals(ps2) is True

    ps2 = PowerSet()
    ps2.put(4)

    assert ps1.equals(ps2) is False


def test_performance():
    ps1 = PowerSet()
    ps2 = PowerSet()
    for i in range(50000):
        ps1.put(i)
        ps2.put(i + 10000)
    start = time.time()
    ps1.union(ps2)
    ps1.intersection(ps2)
    ps1.difference(ps2)
    ps1.issubset(ps2)
    end = time.time()
    assert end - start < 2

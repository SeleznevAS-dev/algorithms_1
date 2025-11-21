import pytest
from .task_3 import DynArray


def test_insert():
    array = DynArray()
    array.append(1)
    array.append(2)
    array.append(3)
    assert array.capacity - array.count == 13

    array.insert(3, 4)
    assert array[3] == 4
    assert array.capacity - array.count == 12

    for i in range(12):
        array.append(i + 5)
    assert array.capacity - array.count == 0

    array.insert(1, 18)
    assert array[1] == 18
    assert array[2] == 2
    assert array.capacity == 32

    with pytest.raises(IndexError):
        array.insert(-1, 20)

    with pytest.raises(IndexError):
        array.insert(20, 20)


def test_delete():
    array = DynArray()
    array.append(1)
    array.append(2)
    array.append(3)
    assert array.capacity - array.count == 13

    array.delete(1)
    assert array[1] == 3
    assert array[0] == 1
    assert array.capacity == 16
    assert array.count == 2

    for i in range(15):
        array.append(i + 4)
    assert array.capacity == 32

    array.delete(0)
    assert array[0] == 3
    assert array.capacity == 32
    array.delete(0)
    assert array[0] == 4
    assert array.capacity == 21

    with pytest.raises(IndexError):
        array.delete(-1)

    with pytest.raises(IndexError):
        array.delete(20)

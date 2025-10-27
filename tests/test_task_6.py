from tasks.task_6 import TRC_sort


def test_regression():
    assert TRC_sort([2, 1, 0]) == [0, 1, 2]
    assert TRC_sort([0, 1, 2, 1, 0, 2]) == [0, 0, 1, 1, 2, 2]

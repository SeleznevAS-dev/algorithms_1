from tasks.task_3 import EEC_help


def test_regression():
    assert EEC_help([1, 2, 3], [1, 2, 3, 4]) is False
    assert EEC_help([1, 2, 3], [1, 2, 3]) is True
    assert EEC_help([1, 3, 2], [1, 2, 3]) is True
    assert EEC_help([1, 3, 2, 3], [1, 2, 2, 3]) is False
    assert EEC_help([1, 1], [1, 1]) is True

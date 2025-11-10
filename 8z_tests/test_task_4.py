from tasks.task_4 import artificial_muscle_fibers


def test_regression():
    assert artificial_muscle_fibers([1, 2, 3, 4, 5]) == 0
    assert artificial_muscle_fibers([1, 2, 3, 2, 1]) == 2
    assert artificial_muscle_fibers([1, 2, 3, 2, 1, 2, 4, 2, 1]) == 2
    assert artificial_muscle_fibers([32000, 32000]) == 1

from tasks.task_8 import army_communication_matrix


def test_3x3():
    assert army_communication_matrix(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == "1 1 2"

def test_4x4():
    assert (
        army_communication_matrix(
            4, [[1, 9, 2, 3], [4, 8, 5, 6], [0, 7, 1, 2], [0, 0, 0, 0]]
        )
        == "1 0 3"
    )

from tasks.task_2 import digital_rain


def test_regression():
    assert digital_rain("1111000") == "111000"
    assert digital_rain("11101000") == "11101000"
    assert digital_rain("011111110") == "10"
    assert digital_rain("11111111") == ""
    assert digital_rain("0111111100") == "1100"

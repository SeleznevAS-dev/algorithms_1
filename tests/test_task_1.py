from tasks.task_1 import white_walkers


def test_regression():
    assert white_walkers("axxb6===4xaf5===eee5") is True
    assert white_walkers("5==ooooooo=5=5") is False
    assert white_walkers("abc=7==hdjs=3gg1=======5") is True
    assert white_walkers("aaS=8") is False
    assert white_walkers("9===1===9===1===9") is True

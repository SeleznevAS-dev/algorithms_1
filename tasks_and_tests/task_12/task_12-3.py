from .task_12 import NativeCache


def test_NativeCache():
    cache = NativeCache(3)

    assert cache.put("a", "a") in [0, 1, 2]
    assert cache.put("b", "b") in [0, 1, 2]
    assert cache.put("c", "c") in [0, 1, 2]
    assert cache.hits == [0, 0, 0]

    assert cache.get("a") == "a"
    assert cache.get("b") == "b"
    assert cache.hits == [0, 1, 1]

    assert cache.put("d", "d") in [0, 1, 2]
    assert cache.get("c") is None

    assert cache.get("b") == "b"
    assert cache.get("d") == "d"
    assert cache.get("d") == "d"
    assert cache.hits == [2, 1, 2]

    assert cache.put("e", "e") in [0, 1, 2]

    assert cache.get("a") is None
    assert cache.hits == [2, 0, 2]

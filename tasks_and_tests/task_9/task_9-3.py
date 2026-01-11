from .task_9 import NativeDictionary


def test_hash_fun():
    nd = NativeDictionary(17)

    assert nd.hash_fun("abc") == 5
    assert nd.hash_fun("abcd") == 3
    assert nd.hash_fun("abcde") == 2


def test_put():
    nd = NativeDictionary(17)
    assert nd.put("abc", 1) == 5
    assert nd.get("abc") == 1

    assert nd.put("abcd", 1) == 3
    assert nd.get("abcd") == 1

    assert nd.put("abc", 2) == 5
    assert nd.get("abc") == 2

    for i in range(100):
        nd.put(f"{i}", i)


def test_is_key():
    nd = NativeDictionary(17)
    nd.put("abc", 1)
    assert nd.is_key("abc") is True
    assert nd.is_key("abcd") is False


def test_get():
    nd = NativeDictionary(17)
    assert nd.put("abc", 1) == 5
    assert nd.get("abc") == 1
    assert nd.get("abcd") is None

    assert nd.put("abcd", 1) == 3
    assert nd.get("abcd") == 1

    assert nd.put("abc", 2) == 5
    assert nd.get("abc") == 2

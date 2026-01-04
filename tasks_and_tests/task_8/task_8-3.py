from .task_8 import HashTable


def test_hash_fun():
    ht = HashTable(17, 3)
    assert ht.hash_fun("abc") == 5
    assert ht.hash_fun("abcd") == 3
    assert ht.hash_fun("abcde") == 2


def test_seek_slot():
    ht = HashTable(17, 3)
    assert ht.seek_slot("abc") == ht.hash_fun("abc")

    index = ht.hash_fun("abc")
    ht.slots[index] = "test"
    assert ht.seek_slot("abc") == index + ht.step


def test_put_stores_value_and_returns_slot_index():
    ht = HashTable(17, 3)
    index = ht.put("abc")
    assert index == ht.hash_fun("abc")
    assert ht.slots[index] == "abc"

    new_index = ht.seek_slot("abc")

    assert new_index == index + ht.step


def test_find_returns_index_for_existing_value():
    ht = HashTable(17, 3)
    put_index = ht.put("abc")
    assert ht.find("abc") == put_index

    new_put_index = ht.put("abc")

    assert new_put_index == put_index + ht.step
    assert ht.find("abc") == put_index
